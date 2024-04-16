from rest_framework import serializers

from apps.donation.models import Customer, Donation


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = "__all__"
        ref_name = "Donation"


class CustomerSerializer(serializers.ModelSerializer):
    donations = DonationSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = "__all__"
        ref_name = "Customer"
