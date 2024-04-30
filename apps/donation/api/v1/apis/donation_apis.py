import logging

import stripe
from django.conf import settings
from django.db import transaction
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from rest_framework import status, views
from rest_framework.response import Response

from apps.donation.models import Customer, Payment

stripe.api_key = settings.STRIPE_SECRET_KEY


class ForumView(TemplateView):
    template_name = "donation/checkout.html"


class SuccessView(TemplateView):
    template_name = "donation/success.html"


class CancelledView(TemplateView):
    template_name = "donation/cancelled.html"


class PaymentView(views.APIView):
    def post(self, request):
        payment_method_id = request.data["payment_method_id"]
        category = request.data["category"]
        first_name = request.data["first_name"]
        last_name = request.data["last_name"]
        email = request.data["email"]
        amount = request.data["amount"]  # Сумма в центах, например, 1000 центов = $10.00

        print(f"category: {category}")
        print(f"Name: {first_name} - {last_name}\nEmail: {email}\nAmount: {amount}")

        try:
            with transaction.atomic():
                intent = stripe.PaymentIntent.create(
                    amount=amount,
                    currency="usd",
                    description="Example charge",
                    payment_method=payment_method_id,
                    confirm=True,
                    return_url="http://127.0.0.1:8000/api/v1/donations/success/",
                )
                create_or_update_customer_in_database(
                    category=category,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    amount=int(amount),
                    intent_id=intent.id,
                )
            return Response({"message": "Оплата прошла успешно"})
        except stripe.error.CardError as e:
            body = e.json_body
            err = body.get("error", {})
            return Response({"message": f'Ошибка: {err.get("message")}'}, status=status.HTTP_400_BAD_REQUEST)


def create_or_update_customer_in_database(category, first_name, last_name, email, amount, intent_id):
    if Customer.objects.filter(email=email).exists():
        customer = Customer.objects.get(email=email)
        Payment.objects.create(customer=customer, amount=amount, intent_id=intent_id)
        logging.warning("Payment created")
    else:
        customer = Customer.objects.create(
            category=category,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        Payment.objects.create(customer=customer, amount=amount, intent_id=intent_id)
        logging.warning("Customer and Payment created")


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event["type"] == "checkout.session.completed":
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
