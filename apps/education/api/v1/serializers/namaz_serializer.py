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
        fields = ("id", "namaz_type", "gender", "explanation_text", "sura_text", "audio", "images")


class NamazCreateUpdateSerializer(serializers.ModelSerializer):
    images = ImageWriteSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        fields = ("id", "namaz_type", "gender", "explanation_text", "sura_text", "audio", "images")

    def create(self, validated_data):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])
        namaz = Namaz.objects.create(**validated_data)
        for image_data in images_data:
            NamazImage.objects.create(namaz=namaz, image=image_data)
        return namaz

    def update(self, instance, validated_data):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])
        instance = super().update(instance, validated_data)

        instance.images.all().delete()
        for image_data in images_data:
            NamazImage.objects.create(namaz=instance, image=image_data)
        return instance

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})

        if str(data.get("gender")) not in ["M", "F"]:
            raise ValidationError({"gender": "Поле 'gender' должно иметь значение 'M'(Male) или 'F'(Female)."})
        return data
