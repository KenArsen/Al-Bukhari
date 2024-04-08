from rest_framework import serializers
from apps.update.models import UpdateModel


class UpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateModel
        fields = '__all__'
