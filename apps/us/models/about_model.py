from ckeditor_uploader.fields import RichTextUploadingField

from apps.common.base import BaseModel


class About(BaseModel):
    content = RichTextUploadingField()

    def __str__(self):
        return f"About ID: {self.id}"
