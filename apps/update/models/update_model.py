from django.db import models


class UpdateModel(models.Model):
    image = models.ImageField(upload_to='updates/', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title[:30]
