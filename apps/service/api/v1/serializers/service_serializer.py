from rest_framework import serializers

from apps.service.models import Service, ServiceImage


class ServiceSendSerializer(serializers.Serializer):
    service = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000, allow_blank=True)

    class Meta:
        ref_name = "ServiceSend"


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = "__all__"
        ref_name = "ServiceImage"


class ServiceReadSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"
        ref_name = "ServiceRead"


class ServiceWriteSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        exclude = ("created_at", "updated_at", "id")
        ref_name = "ServiceWrite"

    def save_images(self, instance, is_update=False):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])

        if is_update and images_data:
            instance.images.all().delete()

        for image_data in images_data:
            ServiceImage.objects.create(service=instance, image=image_data)

    def create(self, validated_data):
        service = Service.objects.create(**validated_data)
        self.save_images(service)
        return service

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        self.save_images(instance, is_update=True)
        return instance
