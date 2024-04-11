from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from rest_framework.exceptions import ValidationError

from apps.common.base import BaseModel
from apps.education.utils import NamazType


class Ghusl(models.Model):
    content = CKEditor5Field("Content", config_name="extends")

    def __str__(self):
        return f'Ghysl ID: {self.id}'


class Taharat(models.Model):
    content = CKEditor5Field("Content", config_name="extends")
    audio = models.FileField(upload_to="audio/", max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Taharat ID: {self.id}'

    def clean(self):
        if len(str(self.audio)) > 10:
            raise ValidationError({"audio": "Длина аудиофайла не должна превышать 255 символов."})


class Namaz(BaseModel):
    namaz_type = models.CharField(max_length=255, choices=NamazType.choices, default=NamazType.FAJR)
    gender = models.CharField(max_length=255, default="male")

    namaz_number = models.SmallIntegerField(default=1)

    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    prayer_part1 = models.CharField(max_length=255, blank=True, null=True)
    prayer_part2 = models.TextField(blank=True, null=True)

    transcription = models.TextField(blank=True, null=True)
    arab = models.TextField(blank=True, null=True)
    mentally = models.TextField(max_length=255, blank=True, null=True)

    audio = models.FileField(upload_to="audio/", max_length=255, blank=True, null=True)

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
