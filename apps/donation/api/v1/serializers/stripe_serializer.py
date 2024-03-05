from rest_framework import serializers

from apps.donation.models import Customer


class StripeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
