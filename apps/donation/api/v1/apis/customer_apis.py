import stripe
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.response import Response

from apps.donation.api.v1.serializers import CustomerSerializer
from apps.donation.models import Customer


class CustomerListAPI(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @swagger_auto_schema(
        tags=["Customer"],
        operation_summary="List customers",
        responses={200: CustomerSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CustomerPaymentListAPI(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @swagger_auto_schema(
        tags=["Customer"],
        operation_summary="Retrieve customer payments",
        responses={200: CustomerSerializer(many=True)},
    )
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(pk=kwargs["pk"])
        customer_payments = stripe.PaymentIntent.list(customer=customer.customer_id)
        return Response(customer_payments, status=status.HTTP_200_OK)


class CustomerDetailAPI(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @swagger_auto_schema(
        tags=["Customer"],
        operation_summary="Retrieve a customer",
        responses={200: CustomerSerializer()},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
