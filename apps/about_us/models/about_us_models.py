from django.db import models
from apps.common.base import BaseModel


class About(BaseModel):
    image1 = models.ImageField(name=None, verbose_name="Image1")
    description1 = models.CharField(max_length=255)
    description2 = models.TextField()
    image2 = models.ImageField(name=None, verbose_name="Image2")

    def __str__(self):
        return f"{self.image1}"
