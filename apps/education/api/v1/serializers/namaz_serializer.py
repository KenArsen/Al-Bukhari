from rest_framework import serializers
from apps.education.models.namaz_model import (
    GhuslAndTaharat,
    Namaz,
)


class GhuslAndTaharatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhuslAndTaharat
        fields = "__all__"


class NamazSerializer(serializers.Serializer):
    class Meta:
        model = Namaz
        fields = "__all__"
