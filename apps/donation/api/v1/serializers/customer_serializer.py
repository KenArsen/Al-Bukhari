from rest_framework import serializers

from apps.donation.models import Customer, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        ref_name = "Payment"


class CustomerSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"
        ref_name = "Customer"
