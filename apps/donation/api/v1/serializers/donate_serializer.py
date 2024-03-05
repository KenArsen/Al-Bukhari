from rest_framework import serializers

from apps.donation.models import Donate


class DonateSerializer(serializers.Serializer):
    category = serializers.ChoiceField(choices=Donate.Category.choices)
    frequency = serializers.ChoiceField(choices=Donate.Frequency.choices)
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    address_1 = serializers.CharField(max_length=255)
    address_2 = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    country = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    state = serializers.CharField(max_length=255)
    zip_code = serializers.CharField(max_length=255)
    comments = serializers.CharField(allow_blank=True, allow_null=True)

    def create(self, validated_data):
        return Donate.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get("category", instance.category)
        instance.frequency = validated_data.get("frequency", instance.frequency)
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.email = validated_data.get("email", instance.email)
        instance.address_1 = validated_data.get("address_1", instance.address_1)
        instance.address_2 = validated_data.get("address_2", instance.address_2)
        instance.country = validated_data.get("country", instance.country)
        instance.city = validated_data.get("city", instance.city)
        instance.state = validated_data.get("state", instance.state)
        instance.zip_code = validated_data.get("zip_code", instance.zip_code)
        instance.comments = validated_data.get("comments", instance.comments)
        instance.save()
        return instance
