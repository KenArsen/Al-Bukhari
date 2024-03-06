from rest_framework import serializers
from apps.us.models.about_us_models import About


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

