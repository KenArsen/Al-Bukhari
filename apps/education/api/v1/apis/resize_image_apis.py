from io import BytesIO

from django.core.files.base import ContentFile
from PIL import Image
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.education.models import NamazImage


class ResizeImageView(APIView):
    class ResizeImageSerializer(serializers.Serializer):
        width = serializers.IntegerField()
        height = serializers.IntegerField()

    def post(self, request, *args, **kwargs):
        serializer = self.ResizeImageSerializer(data=request.data)
        if serializer.is_valid():
            width = serializer.validated_data["width"]
            height = serializer.validated_data["height"]

            images = NamazImage.objects.all()

            for image in images:
                img = Image.open(image.image)
                resized_img = img.resize((width, height))
                output = BytesIO()
                resized_img.save(output, format="PNG")

                image.image.save(image.image.name, ContentFile(output.getvalue()), save=True)

            return Response({"message": "Размеры изображений успешно изменены"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
