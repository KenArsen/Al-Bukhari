# Generated by Django 5.0.2 on 2024-04-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0005_namazbegin_alter_namaz_arab_alter_namaz_prayer_part2_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NamazBegin',
        ),
        migrations.AddField(
            model_name='namaz',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='namaz',
            name='mentally',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='namaz',
            name='namaz_number',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='namaz',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='namaz',
            name='arab',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='namaz',
            name='audio',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='audio/'),
        ),
        migrations.AlterField(
            model_name='namaz',
            name='prayer_part1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='namaz',
            name='prayer_part2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='namaz',
            name='transcription',
            field=models.TextField(blank=True, null=True),
        ),
    ]
