from django.contrib import admin

from .models import Customer, Payment


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "first_name", "last_name", "email")
    list_display_links = ("id", "category", "first_name", "last_name", "email")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "amount", "intent_id")
    list_display_links = ("id", "customer", "amount", "intent_id")
