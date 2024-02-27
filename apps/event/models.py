from django.db import models

from apps.common.base import BaseModel
from apps.image.models import Image


class Event(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Event Title")
    organizer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Organizer")
    email = models.EmailField(blank=True, null=True, verbose_name="Contact Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Contact Phone")
    more = models.TextField(blank=True, null=True, verbose_name="More")
    date = models.DateTimeField(blank=True, null=True, verbose_name="Date")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address")
    images = models.ManyToManyField(Image, blank=True, verbose_name="Images")

    def __str__(self):
        return f"Organizer: {self.organizer}"
