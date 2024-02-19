from .models import Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
<<<<<<< HEAD
        fields = ('id', 'image')
=======
        fields = ("id", "image")
>>>>>>> 24677ec (added STATICFILES_DIRS)

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None
