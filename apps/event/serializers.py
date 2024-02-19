from rest_framework import serializers
from apps.event.models import Event
from apps.image.serializers import ImageSerializer


class EventSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
<<<<<<< HEAD
        fields = ('title', 'organizer', 'email', 'phone', 'more', 'date', 'address', 'images')
=======
        fields = ("title", "organizer", "email", "phone", "more", "date", "address", "images")
>>>>>>> 24677ec (added STATICFILES_DIRS)
