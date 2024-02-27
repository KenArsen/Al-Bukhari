from rest_framework import serializers
from apps.education.models.education_model import Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
