from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http.response import JsonResponse, HttpResponse
from rest_framework.response import Response

import stripe
import json

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'donation/express.html'


class SuccessView(TemplateView):
    template_name = 'donation/success.html'


class CancelledView(TemplateView):
    template_name = 'donation/cancelled.html'


@csrf_exempt
@api_view(['POST'])
def create_checkout_session(request):
    try:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        data = json.loads(request.body)
        # intent = stripe.PaymentIntent.create(
        #     amount=calculate_order_amount(data['items']),
        #     currency='usd',
        #     automatic_payment_methods={
        #         'enabled': True,
        #     },
        # )
        # return Response({
        #     'clientSecret': intent.client_secret
        # })
        return Response({
            'clientSecret': 'pi_3P6UvZFtBaQUT0WN0bmsddH1_secret_anbvbJZOpU8RnRV4QrgLPN7tB'
        })
    except Exception as e:
        return Response({'error': str(e)}, status=403)


def calculate_order_amount(items):
    return 1400


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: run some custom code here

    return HttpResponse(status=200)
