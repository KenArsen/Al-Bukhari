from django.db import models

from apps.common import BaseModel


class Service(BaseModel):
    icon = models.ImageField(upload_to="services/icons/")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class ServiceImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return f"{self.service}"
