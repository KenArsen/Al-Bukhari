from rest_framework import serializers
from apps.education.models import NamazBegin


class NamazBeginSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazBegin
        fields = '__all__'
