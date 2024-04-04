from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models import Ghusl


class GhuslSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghusl
        fields = ("id", "content")

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})
        return data
