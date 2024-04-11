from rest_framework import serializers

from apps.faq.models import Faq


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = "__all__"
        ref_name = "FAQ"
