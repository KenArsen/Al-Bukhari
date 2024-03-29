from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from rest_framework.exceptions import ValidationError

from apps.common.base import BaseModel
from apps.education.utils import NamazType


class GhuslAndTaharat(BaseModel):
    content = CKEditor5Field("Content", config_name="extends")
    audio = models.FileField(upload_to="audio/", max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.__class__.__name__}"

    def clean(self):
        if len(str(self.audio)) > 10:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})


class NamazBegin(BaseModel):
    namaz_type = models.CharField(max_length=255, choices=NamazType.choices, default=NamazType.FAJR)
    gender = models.CharField(max_length=255, default="male")
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prayer_part1 = models.CharField(max_length=255)
    prayer_part2 = models.TextField()
    mentally = models.CharField(max_length=255)
    image = models.ImageField(upload_to="namaz/")

    def __str__(self):
        return f"{self.namaz_type}"


class Namaz(BaseModel):
    namaz_type = models.CharField(max_length=255, choices=NamazType.choices, default=NamazType.FAJR)
    gender = models.CharField(max_length=255, default="male")
    prayer_part1 = models.CharField(max_length=255)
    prayer_part2 = models.TextField()
    transcription = models.TextField()
    arab = models.TextField()
    audio = models.FileField(upload_to="audio/", max_length=255)

    def __str__(self):
        return f"{self.namaz_type}"

    def clean(self):
        if len(str(self.audio)) > 255:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})

        if self.gender not in ["male", "female"]:
            raise ValidationError({"gender": "Поле 'gender' должно иметь значение 'male' или 'female'"})


class NamazImage(models.Model):
    namaz = models.ForeignKey(Namaz, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="namaz/")

    def __str__(self):
        return f"ID: {self.id} - {self.image.name[:20]}"
