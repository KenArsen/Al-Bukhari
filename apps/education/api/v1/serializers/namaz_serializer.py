import io

from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.education.models import Namaz, NamazImage


class ImageReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class ImageWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = NamazImage
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.image.url if obj.image else None


class NamazSerializer(serializers.ModelSerializer):
    images = ImageReadSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        fields = "__all__"


class NamazCreateUpdateSerializer(serializers.ModelSerializer):
    images = ImageWriteSerializer(many=True, read_only=True)

    class Meta:
        model = Namaz
        exclude = ("id",)

    def create(self, validated_data):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])
        namaz = Namaz.objects.create(**validated_data)
        for image_data in images_data:
            image = Image.open(image_data)
            resized_image = image.resize((300, 200))
            output = io.BytesIO()
            resized_image.save(output, format="PNG")
            output.seek(0)
            image_name = image_data.name
            image_file = InMemoryUploadedFile(output, None, image_name, "image/png", output.getbuffer().nbytes, None)
            NamazImage.objects.create(namaz=namaz, image=image_file)
        return namaz

    def update(self, instance, validated_data):
        request = self.context.get("request")
        images_data = request.FILES.getlist("images", [])
        instance = super().update(instance, validated_data)

        instance.images.all().delete()
        for image_data in images_data:
            image = Image.open(image_data)
            resized_image = image.resize((300, 200))
            output = io.BytesIO()
            resized_image.save(output, format="PNG")
            output.seek(0)
            image_name = image_data.name
            image_file = InMemoryUploadedFile(output, None, image_name, "image/png", output.getbuffer().nbytes, None)
            NamazImage.objects.create(namaz=instance, image=image_file)
        return instance

    def validate(self, data):
        if len(str(data.get("audio"))) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})

        if str(data.get("gender")) not in ["male", "female"]:
            raise ValidationError({"gender": "Поле 'gender' должно иметь значение 'male' или 'female'"})
        return data
