from django.db import models
from apps.common.base import BaseModel


class Image(BaseModel):
<<<<<<< HEAD
    image = models.ImageField(upload_to='images/', verbose_name='Image', blank=True, null=True)

    def __str__(self):
        return f'Image ID: {self.id}'
=======
    image = models.ImageField(upload_to="images/", verbose_name="Image", blank=True, null=True)

    def __str__(self):
        return f"Image ID: {self.id}"
>>>>>>> 24677ec (added STATICFILES_DIRS)
