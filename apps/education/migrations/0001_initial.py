# Generated by Django 5.0.2 on 2024-02-27 15:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('NAMAZ TRAINING', 'NAMAZ TRAINING'), ('ABOUT ISLAM', 'ABOUT_ISLAM'), ('INSPIRATIONAL STORIES', 'INSPIRATIONAL STORIES'), ('ABOUT QURAN', 'ABOUT QURAN'), ('QURAN LEANING', 'QURAN LEANING')], default='NAMAZ TRAINING', max_length=255)),
                ('content', ckeditor.fields.RichTextField()),
                ('audio', models.FileField(blank=True, null=True, upload_to='education/audio')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GhuslAndTaharat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('audio', models.FileField(blank=True, null=True, upload_to='education/audio')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Namaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('namaz_type', models.CharField(choices=[('FAJR', 'FAJR'), ('ZUHR', 'ZUHR'), ('ASR', 'ASR'), ('MAGHREB', 'MAGHREB'), ('ISHA', 'ISHA'), ('VITR', 'VITR')], default='FAJR', max_length=255)),
                ('explanation_text', models.TextField()),
                ('sura_text', models.TextField()),
                ('audio_file', models.FileField(upload_to='namaz_audio/')),
                ('photo', models.ManyToManyField(related_name='namaz_images', to='image.image')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
