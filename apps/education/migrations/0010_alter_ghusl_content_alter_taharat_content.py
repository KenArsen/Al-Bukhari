# Generated by Django 5.0.2 on 2024-04-22 11:40

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0009_rename_educationlist_educationcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ghusl',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='taharat',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
