import logging

import stripe
from django.conf import settings
from django.db import transaction
from django.http.response import HttpResponse
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

        try:
            with transaction.atomic():
                intent = stripe.PaymentIntent.create(
                    amount=amount,
                    currency="usd",
                    description="Example charge",
                    payment_method=payment_method_id,
                    confirm=True,
                    return_url=f"{settings.DOMAIN_NAME}/api/v1/donations/success/",
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


class StripeWebhookView(views.APIView):
    def post(self, request):
        payload = request.body
        sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
        endpoint_secret = settings.STRIPE_ENDPOINT_SECRET

        try:
            event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
        except ValueError as e:
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            return HttpResponse(status=400)

        # Обработка события checkout.session.completed
        if event["type"] == "checkout.session.completed":
            # Получение данных платежа из события
            payment_intent_id = event["data"]["object"]["payment_intent"]
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            payment_method_id = payment_intent["payment_method"]
            amount = payment_intent["amount"]
            category = "your_category"
            first_name = "your_default_first_name"
            last_name = "your_default_last_name"
            email = "your_default_email@example.com"

            # Вызов метода PaymentView.post() для обработки платежа
            payment_view = PaymentView()
            request.data = {
                "payment_method_id": payment_method_id,
                "category": category,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "amount": amount,
            }
            response = payment_view.post(request)

            if response.status_code == status.HTTP_200_OK:
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        else:
            # Другие обработки событий Stripe, если необходимо
            return HttpResponse(status=200)
