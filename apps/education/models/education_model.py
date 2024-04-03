from django.db import models


class Education(models.Model):
    category = models.CharField(max_length=255)
    title = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.category}"


class EducationList(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name="list")
    description = models.TextField()
    image = models.ImageField(upload_to="education/", null=True, blank=True)

    def __str__(self):
        return f"{self.education.category}"
