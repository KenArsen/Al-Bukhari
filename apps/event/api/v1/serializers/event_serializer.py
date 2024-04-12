from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.event.models import Event, EventImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = "__all__"
        ref_name = "EventImage"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class EventReadSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ("id", "title", "organizer", "email", "phone", "more", "date", "address", "images")
        ref_name = "EventRead"


class EventWriteSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Event
        fields = ("id", "title", "organizer", "email", "phone", "more", "date", "address", "images")
        ref_name = "EventWrite"

    def save_images(self, instance, is_update=False):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])

        if is_update:
            instance.images.all().delete()

        for image_data in images_data:
            EventImage.objects.create(event=instance, image=image_data)

    def create(self, validated_data):
        event = Event.objects.create(**validated_data)
        self.save_images(event)
        return event

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        self.save_images(instance, is_update=True)
        return instance

    def validate(self, data):
        if len(str(data.get("images"))) > 255:
            raise ValidationError({"images": "Длина изображений не должна превышать 255 символов."})
        return data
