from PIL import Image
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.education.models import NamazImage


class ResizeImagesAPI(APIView):
    def post(self, request):
        try:
            new_width = int(request.data.get("width"))
            new_height = int(request.data.get("height"))
        except (TypeError, ValueError):
            return Response("Invalid width or height", status=status.HTTP_400_BAD_REQUEST)

        images = NamazImage.objects.all()

        for image in images:
            img = Image.open(image.image)
            img_resized = img.resize((new_width, new_height), Image.LANCZOS)

            img_resized.save(image.image.path)

            img.close()
            img_resized.close()

        return Response("Images resized successfully", status=status.HTTP_200_OK)
