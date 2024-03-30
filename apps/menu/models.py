from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='menu/')

    def __str__(self):
        return self.name
