from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.event.models import Event, EventImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ("id", "title", "organizer", "email", "phone", "more", "date", "address", "images")


class EventCreateUpdateSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Event
        fields = ("id", "title", "organizer", "email", "phone", "more", "date", "address", "images")

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])
        event = Event.objects.create(**validated_data)
        for image_data in images_data:
            EventImage.objects.create(event=event, **image_data)
        return event

    def update(self, instance, validated_data):
        images_data = validated_data.pop("images", [])
        instance = super().update(instance, validated_data)

        instance.images.all().delete()
        for image_data in images_data:
            EventImage.objects.create(event=instance, **image_data)
        return instance

    def validate(self, data):
        if len(str(data.get("images"))) > 255:
            raise ValidationError({"images": "Длина изображений не должна превышать 255 символов."})
        return data
