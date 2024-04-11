from rest_framework import serializers

from apps.update.models import Update


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = "__all__"
        ref_name = "Update"
