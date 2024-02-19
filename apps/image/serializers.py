from .models import Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'image')

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None
