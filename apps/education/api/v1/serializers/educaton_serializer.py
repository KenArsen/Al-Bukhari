from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models.education_model import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("id", "category", "content", "audio")

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})
        return data
