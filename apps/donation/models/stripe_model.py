from django.db import models

from apps.common import BaseModel


class Customer(BaseModel):
    customer_id = models.CharField(max_length=255, unique=True)
    payment_id = models.CharField(max_length=255, unique=True)

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.customer_id}"
