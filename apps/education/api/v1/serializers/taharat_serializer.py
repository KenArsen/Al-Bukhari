from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models import Taharat


class TaharatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taharat
        fields = ("id", "content", "audio")

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})
        return data
