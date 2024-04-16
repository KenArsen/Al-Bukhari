import logging

import stripe
from django.conf import settings
from django.views.generic.base import TemplateView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.response import Response

from apps.donation.models import Customer, Donation

stripe.api_key = settings.STRIPE_SECRET_KEY


class ForumView(TemplateView):
    template_name = "donation/checkout.html"


class DonateCreateAPI(views.APIView):
    data = {}

    @swagger_auto_schema(
        tags=["Donate"],
        operation_summary="Create a donation",
        responses={200: "Success response", 400: "Bad request"},
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

        try:
            customer_id = get_or_create_customer(self.data["email"], self.data["first_name"], self.data["last_name"])
            payment_intent = create_payment_intent(
                amount, payment_method_id, customer_id, self.data["first_name"], self.data["last_name"]
            )
            create_or_update_customer_in_database(
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


def get_or_create_customer(email, first_name, last_name):
    existing_customer = stripe.Customer.list(email=email).data
    if existing_customer:
        return existing_customer[0].id
    else:
        customer = stripe.Customer.create(
            name=f"{first_name} {last_name}",
            email=email,
        )
        return customer.id


def create_payment_intent(amount, payment_method_id, customer_id, first_name, last_name):
    return stripe.PaymentIntent.create(
        amount=int(amount) * 100,
        currency="usd",
        payment_method=payment_method_id,
        confirmation_method="manual",
        confirm=True,
        customer=customer_id,
        description=f"Donation from {first_name} {last_name}",
        return_url=f"{settings.DOMAIN_NAME}/api/v1/events/",
    )


def create_or_update_customer_in_database(customer_id, payment_method_id, first_name, last_name, email, amount):
    if Customer.objects.filter(customer_id=customer_id).exists():
        customer = Customer.objects.get(customer_id=customer_id)
        Donation.objects.create(customer=customer, amount=amount, payment_id=payment_method_id)
        logging.warning("Donation created")
    else:
        customer = Customer.objects.create(
            customer_id=customer_id,
            name=f"{first_name} {last_name}",
            email=email,
        )
        Donation.objects.create(customer=customer, amount=int(amount) * 100, payment_id=payment_method_id)
        logging.warning("Customer and Donation created")
