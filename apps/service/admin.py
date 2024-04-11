from django.contrib import admin

from apps.service.models import Service, ServiceImage


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    inlines = [ServiceImageInline]


@admin.register(ServiceImage)
class ServiceImageAdmin(admin.ModelAdmin):
    list_display = ("id", "service")
    list_display_links = ("id", "service")
