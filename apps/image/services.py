import logging

from rest_framework.exceptions import ValidationError

from apps.image.serializers import ImageSerializer


def _add_image(request, serializer):
    if serializer.is_valid():
        obj_instance = serializer.save()
        images = request.FILES.getlist("images", [])
        for image in images:
            for img in obj_instance.images.all():
                img.delete()
            image_serializer = ImageSerializer(data={"image": image})
            if image_serializer.is_valid():
                image_instance = image_serializer.save()
                obj_instance.images.add(image_instance)
            else:
                raise ValidationError({"error": image_serializer.errors})
        return serializer
    else:
        raise ValidationError({"error": serializer.errors})


class ImageService:
    def __init__(self, serializer=None, repository=None, obj=None):
        self.serializer = serializer
        self.repository = repository
        self.obj = obj

    def create_image(self, request):
        obj_serializer = self.serializer(data=request.data)
        return _add_image(request=request, serializer=obj_serializer)

    def update_image(self, request, pk):
        instance = self.repository.get_by_id(pk=pk)
        obj_serializer = self.serializer(instance=instance, data=request.data)
        return _add_image(request=request, serializer=obj_serializer)

    def delete_image(self, pk):
        try:
            instance = self.repository.get_by_id(pk=pk)
            related_images = instance.images.all()
            for image in related_images:
                image.delete()
        except self.obj.DoesNotExist:
            logging.warning("Image not found")
