from django.db import models


class Education(models.Model):
    category = models.CharField(max_length=255)
    title = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category}"


class EducationCategory(models.Model):
    class Day(models.TextChoices):
        DEFAULT = 'DEFAULT', 'DEFAULT'
        MONDAY = 'MONDAY', 'MONDAY'
        TUESDAY = 'TUESDAY', 'TUESDAY'
        WEDNESDAY = 'WEDNESDAY', 'WEDNESDAY'
        THURSDAY = 'THURSDAY', 'THURSDAY'
        FRIDAY = 'FRIDAY', 'FRIDAY'
        SATURDAY = 'SATURDAY', 'SATURDAY'
        SUNDAY = 'SUNDAY', 'SUNDAY'

    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name="list")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="education/", null=True, blank=True)

    day = models.CharField(choices=Day.choices, default=Day.DEFAULT, max_length=255, blank=True, null=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"ID: {self.id} - CATEGORY - {self.education.category}"

    def save(self, *args, **kwargs):
        try:
            if self.day != 'DEFAULT':
                quran_leaning = EducationCategory.objects.get(day=self.day)
                quran_leaning.start_time = self.start_time
                quran_leaning.end_time = self.end_time
                quran_leaning.description = self.description
                quran_leaning.save()
            else:
                raise EducationCategory.DoesNotExist
        except EducationCategory.DoesNotExist:
            super().save(*args, **kwargs)
