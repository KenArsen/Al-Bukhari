from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Update(models.Model):
    image = models.ImageField(upload_to="updates/", null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = CKEditor5Field("Content", config_name="extends", default='')

    def __str__(self):
        return self.title[:30]
