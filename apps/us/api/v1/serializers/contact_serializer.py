from rest_framework import serializers

from apps.us.models import Contact, Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ("id", "type_url", "title", "url", "icon", "contact")
        read_only_fields = ("id",)
        ref_name = "ContactUrlUs"


class ContactSerializer(serializers.ModelSerializer):
    urls = UrlSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = ("id", "image1", "urls")
        read_only_fields = ("id", "created_at", "updated_at")
        ref_name = "ContactUS"
