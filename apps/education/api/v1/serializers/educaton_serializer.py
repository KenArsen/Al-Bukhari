from rest_framework import serializers

from apps.education.models import Education, EducationList


class EducationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationList
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    list = EducationCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = "__all__"
