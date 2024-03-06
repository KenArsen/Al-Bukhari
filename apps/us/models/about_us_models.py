from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from apps.common.base import BaseModel


class About(BaseModel):
    about = CKEditor5Field("Content", config_name="extends")

    def __str__(self):
        return f"{self.id}"