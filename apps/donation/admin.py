from django.contrib import admin

from .models import Customer, Donation


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_id", "name", "email")
    list_display_links = ("id", "customer_id", "name", "email")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ("id", "customer", "payment_id")
    list_display_links = ("id", "customer", "payment_id")
