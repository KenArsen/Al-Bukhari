from django.db import models

from apps.common.base import BaseModel


class Event(BaseModel):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Event Title")
    organizer = models.CharField(max_length=255, blank=True, null=True, verbose_name="Organizer")
    email = models.EmailField(blank=True, null=True, verbose_name="Contact Email")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Contact Phone")
    more = models.TextField(blank=True, null=True, verbose_name="More")
    start_date = models.DateTimeField(blank=True, null=True, verbose_name="Start Date")
    end_date = models.DateTimeField(blank=True, null=True, verbose_name="End Date")
    address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address")

    def __str__(self):
        return f"Organizer: {self.organizer}"


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="event/")

    def __str__(self):
        return f"ID: {self.id} - {self.image.name[:20]}"
