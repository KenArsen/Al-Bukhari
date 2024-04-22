from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Update(models.Model):
    image = models.ImageField(upload_to="updates/", null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)

    def __str__(self):
        return self.title[:30]
