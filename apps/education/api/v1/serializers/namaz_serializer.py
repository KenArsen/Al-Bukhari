from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models.namaz_model import GhuslAndTaharat, Namaz
from apps.image.serializers import ImageSerializer


class GhuslAndTaharatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhuslAndTaharat
        fields = ("id", "content", "audio")

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})
        return data


class NamazSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        fields = ("id", "namaz_type", "images", "explanation_text", "sura_text", "audio")

    def validate(self, data):
        if len(str(data.get("images"))) > 255:
            raise ValidationError({"images": "Длина изображений не должна превышать 255 символов."})

        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})

        return data
