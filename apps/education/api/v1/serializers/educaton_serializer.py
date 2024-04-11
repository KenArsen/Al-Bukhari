from rest_framework import serializers

from apps.education.models import Education, EducationList


class EducationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationList
        fields = "__all__"
        ref_name = "EducationList"


class EducationSerializer(serializers.ModelSerializer):
    list = EducationListSerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = "__all__"
        ref_name = "Education"
