from django.contrib import admin

from .models import Update


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
