# Generated by Django 5.0.2 on 2024-04-15 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_ghusl_taharat_delete_ghuslandtaharat'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EducationList',
            new_name='EducationCategory',
        ),
    ]