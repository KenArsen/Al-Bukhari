# Generated by Django 5.0.2 on 2024-04-16 07:48

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0002_rename_updatemodel_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='content',
            field=django_ckeditor_5.fields.CKEditor5Field(default='', verbose_name='Content'),
        ),
    ]