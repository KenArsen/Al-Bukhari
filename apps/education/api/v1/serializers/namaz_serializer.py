from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models import Namaz, NamazImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"


class NamazSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Namaz
        fields = ("id", "namaz_type", "images", "explanation_text", "sura_text", "audio")


class NamazCreateUpdateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, required=False)

    class Meta:
        model = Namaz
        fields = ("id", "namaz_type", "images", "explanation_text", "sura_text", "audio")

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
        if len(str(data.get("images"))) > 255:
            raise ValidationError({"images": "Длина изображений не должна превышать 255 символов."})

        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})
        return data
