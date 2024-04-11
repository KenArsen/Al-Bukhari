from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models import Namaz, NamazImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"
        ref_name = "NamazImage"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class NamazReadSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        exclude = ("created_at", "updated_at")
        ref_name = "NamazRead"


class NamazWriteSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)

    class Meta:
        model = Namaz
        exclude = ("id", "created_at", "updated_at")
        ref_name = "NamazWrite"

    def save_images(self, instance, is_update=False):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])

        if is_update:
            instance.images.all().delete()

        for image_data in images_data:
            NamazImage.objects.create(namaz=instance, image=image_data)

    def create(self, validated_data):
        namaz = Namaz.objects.create(**validated_data)
        self.save_images(namaz)
        return namaz

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        self.save_images(instance, is_update=True)
        return instance

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})

        if str(data.get("gender")) not in ["male", "female"]:
            raise ValidationError({"gender": "Поле 'gender' должно иметь значение 'male' или 'female'"})
        return data
