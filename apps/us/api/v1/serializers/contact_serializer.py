from rest_framework import serializers

from apps.us.models import Contact, Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("id", "title", "url", "icon", "contact")
        read_only_fields = ("id",)


class ContactSerializer(serializers.ModelSerializer):
    urls = UrlSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ("id", "image1", "image2", "urls")
        read_only_fields = ("id", "created_at", "updated_at")
