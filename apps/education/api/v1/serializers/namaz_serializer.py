from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models import Namaz, NamazImage


class ImageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class ImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class NamazSerializer(serializers.ModelSerializer):
    images = ImageReadSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        exclude = ("created_at", "updated_at")


class NamazCreateUpdateSerializer(serializers.ModelSerializer):
    images = ImageWriteSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        exclude = ("id", "created_at", "updated_at")

    def save_images(self, instance, is_update=False):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])

        if is_update:
            instance.images.all().delete()
        for image_data in images_data:
            NamazImage.objects.create(namaz=instance, image=image_data)

    def create(self, validated_data):
        namaz = Namaz.objects.create(**validated_data)
        self.save_images(namaz)
        return namaz

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        self.save_images(instance, is_update=True)
        return instance

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})

        if str(data.get("gender")) not in ["male", "female"]:
            raise ValidationError({"gender": "Поле 'gender' должно иметь значение 'male' или 'female'"})
        return data
