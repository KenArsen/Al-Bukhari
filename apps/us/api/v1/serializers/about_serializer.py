from rest_framework import serializers

from apps.us.models.about_model import About


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        read_only_fields = ["id", "created_at", "updated_at"]
        fields = "__all__"
