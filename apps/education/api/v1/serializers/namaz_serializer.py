from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models import Namaz, NamazImage


class ImageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"


class ImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"


class NamazSerializer(serializers.ModelSerializer):
    images = ImageReadSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        fields = ("id", "namaz_type", "explanation_text", "sura_text", "audio", "images")


class NamazCreateUpdateSerializer(serializers.ModelSerializer):
    images = ImageWriteSerializer(many=True)

    class Meta:
        model = Namaz
        fields = ("id", "namaz_type", "explanation_text", "sura_text", "audio", "images")

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        namaz = Namaz.objects.create(**validated_data)
        for image_data in images_data:
            NamazImage.objects.create(namaz=namaz, **image_data)
        return namaz

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])
        instance = super().update(instance, validated_data)

        instance.images.all().delete()
        for image_data in images_data:
            NamazImage.objects.create(namaz=instance, **image_data)
        return instance

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})
        return data
