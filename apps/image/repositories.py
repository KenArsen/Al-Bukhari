from .models import Image


class ImageRepository:
    @classmethod
    def get_images(cls):
        return Image.objects.all()

    def get_image_by_id(self, image_id):
        return Image.objects.get(id=image_id)
