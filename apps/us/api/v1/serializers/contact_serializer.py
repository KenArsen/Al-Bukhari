from rest_framework import serializers

from apps.us.models import Contact, Url


class ContactSendSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000, allow_blank=True)

    class Meta:
        ref_name = "ContactSend"


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
