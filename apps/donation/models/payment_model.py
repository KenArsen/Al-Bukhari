from django.db import models

from apps.common import BaseModel


class Customer(BaseModel):
    category = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return f"{self.email}"


class Payment(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    intent_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.amount}"
