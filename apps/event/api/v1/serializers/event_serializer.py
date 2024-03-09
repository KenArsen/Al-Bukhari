from rest_framework import serializers

from apps.event.models import Event
from apps.image.serializers import ImageSerializer


class EventSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ("id", "title", "organizer", "email", "phone", "more", "date", "address", "images")
