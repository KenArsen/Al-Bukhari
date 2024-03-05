from django.db import models

from apps.common import BaseModel


class Donate(BaseModel):
    class Category(models.TextChoices):
        GDAS = "GDAS", "General Donation Auto selected"
        GDSMF = "GDSMF", "General Donation(Sadaqa fund)"
        ZAKAT = "ZAKAT", "Zakat"
        FITRA = "FITRA", "Fitra"

    class Frequency(models.TextChoices):
        ONE_TIME = "ONE TIME", "one time"
        MONTHLY = "MONTHLY", "monthly"
        WEEKLY = "WEEKLY", "weekly"
        DAILY = "DAILY", "daily"

    category = models.CharField(max_length=255, choices=Category.choices, default=Category.GDAS)
    frequency = models.CharField(max_length=255, choices=Frequency.choices, default=Frequency.ONE_TIME)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.email}"
