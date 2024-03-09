from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from rest_framework.exceptions import ValidationError

from apps.common.base import BaseModel
from apps.image.models import Image


class GhuslAndTaharat(BaseModel):
    content = CKEditor5Field("Content", config_name="extends")
    audio = models.FileField(upload_to="audio/", max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.__class__.__name__}"

    def clean(self):
        if len(str(self.audio)) > 10:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})


class Namaz(BaseModel):
    class NamazType(models.TextChoices):
        FAJR = "FAJR", "FAJR"
        ZUHR = "ZUHR", "ZUHR"
        ASR = "ASR", "ASR"
        MAGHREB = "MAGHREB", "MAGHREB"
        ISHA = "ISHA", "ISHA"
        VITR = "VITR", "VITR"

    namaz_type = models.CharField(
        max_length=255,
        choices=NamazType.choices,
        default=NamazType.FAJR,
    )
    images = models.ManyToManyField(Image, related_name="namaz_images", max_length=255)
    explanation_text = models.TextField()
    sura_text = models.TextField()
    audio = models.FileField(upload_to="audio/", max_length=255)

    def __str__(self):
        return f"{self.namaz_type}"

    def clean(self):
        if len(str(self.images)) > 255:
            raise ValidationError({"images": "Длина изображений не должна превышать 255 символов."})

        if len(str(self.audio)) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})
