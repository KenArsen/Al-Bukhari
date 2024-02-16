from rest_framework import viewsets

from apps.image.repositories import ImageRepository
from apps.image.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageRepository.get_images()
    serializer_class = ImageSerializer
