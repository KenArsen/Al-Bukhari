from rest_framework import serializers

from apps.update.models import Update


class UpdateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = ('id', 'image', 'title', 'description')
        ref_name = 'UpdateList'


class UpdateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Update
        fields = "__all__"
        ref_name = "Update"
