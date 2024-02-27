from apps.common.base import BaseModel
from django.db import models
from ckeditor.fields import RichTextField


class GhuslAndTaharat(BaseModel):
    content = RichTextField()
    audio = models.FileField(upload_to="education/audio", null=True, blank=True)

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
    audio_file = models.FileField(upload_to="namaz_audio/")

    def __str__(self):
        return f"{self.namaz_type}"
