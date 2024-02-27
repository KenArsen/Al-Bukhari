from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.common.base import BaseModel


class Education(BaseModel):
    class Category(models.TextChoices):
        NAMAZ_TRAINING = "NAMAZ TRAINING", "NAMAZ TRAINING"
        ABOUT_ISLAM = "ABOUT ISLAM", "ABOUT_ISLAM"
        INSPIRATIONAL_STORIES = "INSPIRATIONAL STORIES", "INSPIRATIONAL STORIES"
        ABOUT_QURAN = "ABOUT QURAN", "ABOUT QURAN"
        QURAN_LEANING = "QURAN LEANING", "QURAN LEANING"

    category = models.CharField(max_length=255, choices=Category.choices, default=Category.NAMAZ_TRAINING)
    content = CKEditor5Field("Content", config_name="extends")
    audio = models.FileField(upload_to="education/audio", null=True, blank=True)

    def __str__(self):
        return f"{self.category}"
