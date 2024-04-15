from rest_framework import serializers

from apps.education.models import Education, EducationCategory


class EducationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationCategory
        fields = "__all__"
        ref_name = "EducationCategory"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ("id", "category")
        ref_name = "Education"


class EducationWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        ref_name = "EducationWrite"


class EducationDetailSerializer(serializers.ModelSerializer):
    list = EducationCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Education
        fields = "__all__"
        ref_name = "EducationDetail"
