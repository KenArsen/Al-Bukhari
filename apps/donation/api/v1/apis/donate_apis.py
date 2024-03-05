import logging

import stripe
from django.db.models import Q
from django.views.generic.base import TemplateView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.response import Response

from apps.donation.api.v1.serializers import DonateSerializer, StripeSerializer
from apps.donation.models import Customer, Donate

stripe.api_key = (
    "sk_test_51OjhrkFtBaQUT0WNQVkFceEHafIJrYqlHd5YeTiV3X7IyAuAiWvbcmPfGuevV6bmL34x4InUGc2wscMv5MazJCI500isHgFW2l"
)


class ForumView(TemplateView):
    template_name = "donation/checkout.html"


class CustomerListAPI(views.APIView):
    @swagger_auto_schema(
        operation_description="Retrieve a list of customers.",
        responses={200: StripeSerializer(many=True)},
        tags=["Customer"],
        operation_summary="List customers",
    )
    def get(self, request):
        customers = Customer.objects.all()
        serializer = StripeSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerPaymentAPI(views.APIView):
    @swagger_auto_schema(
        responses={200: StripeSerializer(many=True)},
        tags=["Customer"],
        operation_summary="Retrieve customer payments",
        operation_description="Retrieve payments for a specific customer.",
    )
    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)

        customer_payments = stripe.PaymentIntent.list(customer=customer.customer_id)
        return Response(customer_payments, status=status.HTTP_200_OK)


class CustomerDetailAPI(views.APIView):
    @swagger_auto_schema(
        responses={200: StripeSerializer()},
        tags=["Customer"],
        operation_summary="Retrieve a customer",
        operation_description="Retrieve details of a specific customer.",
    )
    def get(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        serializer = StripeSerializer(customer, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DonateListAPI(views.APIView):
    @swagger_auto_schema(
        responses={200: DonateSerializer(many=True)},
        tags=["Donate"],
        operation_summary="Retrieve a list of donations",
        operation_description="Retrieve a list of recent donations.",
    )
    def get(self, request):
        payments = stripe.PaymentIntent.list(limit=10)
        return Response({"payments": payments})


class DonateCreateAPI(views.APIView):
    data = {}

    @swagger_auto_schema(
        tags=["Donate"],
        operation_summary="Create a donation",
        operation_description="Create a new donation.",
        responses={200: "Success response", 400: "Bad request"},
        request_body=DonateSerializer,
    )
    def post(self, request):
        self.data["category"] = request.data.get("category")
        self.data["frequency"] = request.data.get("frequency")

        self.data["first_name"] = request.data.get("first_name")
        self.data["last_name"] = request.data.get("last_name")
        self.data["phone_number"] = request.data.get("phone_number")
        self.data["email"] = request.data.get("email")

        self.data["address_1"] = request.data.get("address_1")
        self.data["address_2"] = request.data.get("address_2")
        self.data["country"] = request.data.get("country")
        self.data["city"] = request.data.get("city")
        self.data["state"] = request.data.get("state")
        self.data["zip_code"] = request.data.get("zip_code")

        self.data["comments"] = request.data.get("comments")

        amount = request.data.get("amount")
        payment_method_id = request.data.get("payment_method_id")

        if not Donate.objects.filter(email=self.data["email"]).exists():
            donation_serializer = self.create_donation_serializer(data=self.data)
            if not donation_serializer.is_valid():
                return Response(donation_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            donation_serializer.save()
            logging.info("Successfully created donation")
        else:
            logging.warning("Donation already exists")

        try:
            customer_id = self.get_or_create_customer(
                self.data["email"], self.data["first_name"], self.data["last_name"]
            )
            payment_intent = self.create_payment_intent(
                amount, payment_method_id, customer_id, self.data["first_name"], self.data["last_name"]
            )
            self.create_or_update_customer_in_database(
                customer_id,
                payment_method_id,
                self.data["first_name"],
                self.data["last_name"],
                self.data["email"],
                amount,
            )
            return Response({"success": True, "payment": payment_intent})
        except stripe.error.CardError as e:
            body = e.json_body
            err = body["error"]
            return Response("Payment failed: {}".format(err["message"]), status=status.HTTP_400_BAD_REQUEST)
        except stripe.error.StripeError as e:
            error_message = str(e)
            logging.error("Stripe Error:", error_message)
            return Response("Payment failed: " + error_message, status=status.HTTP_400_BAD_REQUEST)

    def create_donation_serializer(self, data):
        return DonateSerializer(data=data)

    def get_or_create_customer(self, email, first_name, last_name):
        existing_customer = stripe.Customer.list(email=email).data
        if existing_customer:
            return existing_customer[0].id
        else:
            customer = stripe.Customer.create(
                name=f"{first_name} {last_name}",
                email=email,
            )
            return customer.id

    def create_payment_intent(self, amount, payment_method_id, customer_id, first_name, last_name):
        return stripe.PaymentIntent.create(
            amount=int(amount) * 100,
            currency="usd",
            payment_method=payment_method_id,
            confirmation_method="manual",
            confirm=True,
            customer=customer_id,
            description=f"Donation from {first_name} {last_name}",
            return_url="http://127.0.0.1:8000/api/v1/events/",
        )

    def create_or_update_customer_in_database(
        self, customer_id, payment_method_id, first_name, last_name, email, amount
    ):
        if not Customer.objects.filter(Q(customer_id=customer_id) | Q(payment_id=payment_method_id)).exists():
            Customer.objects.create(
                customer_id=customer_id,
                payment_id=payment_method_id,
                name=f"{first_name} {last_name}",
                email=email,
                amount=int(amount) * 100,
            )
        else:
            logging.warning("Customer already exists")
