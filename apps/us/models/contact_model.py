from django.db import models

from apps.common.base import BaseModel


class Url(models.Model):
    type_url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=255, blank=True, null=True)
    icon = models.ImageField(upload_to="icons/", blank=True, null=True)
    contact = models.ForeignKey("Contact", on_delete=models.CASCADE, related_name="urls")

    def __str__(self):
        return self.title


class Contact(BaseModel):
    image1 = models.ImageField(upload_to="us/contact/", blank=True, null=True)

    def __str__(self):
        return f" Image ID: {self.id}"
