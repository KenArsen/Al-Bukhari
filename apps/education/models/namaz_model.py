from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.common.base import BaseModel


class GhuslAndTaharat(BaseModel):
    content = CKEditor5Field("Content", config_name="extends")
    audio = models.FileField(upload_to="audio/", null=True, blank=True)

    def __str__(self):
        return f"{self.__class__.__name__}"


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
    photo = models.ManyToManyField("image.Image", related_name="namaz_images")
    explanation_text = models.TextField()
    sura_text = models.TextField()
    audio = models.FileField(upload_to="audio/")

    def __str__(self):
        return f"{self.namaz_type}"
