from rest_framework import serializers

from apps.education.models.namaz_model import GhuslAndTaharat, Namaz
from apps.image.serializers import ImageSerializer


class GhuslAndTaharatSerializer(serializers.ModelSerializer):
    class Meta:
        model = GhuslAndTaharat
        fields = "__all__"


class NamazSerializer(serializers.ModelSerializer):
    photo = ImageSerializer(many=True)

    class Meta:
        model = Namaz
        fields = "__all__"
