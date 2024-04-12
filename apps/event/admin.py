from django.contrib import admin

from apps.event.models import Event, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ("id", "title", "email")
    list_display_links = ("id", "title", "email")
    readonly_fields = ("created_at", "updated_at")
    inlines = [EventImageInline]


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ("id", "event",)
    list_display_links = ("id", "event",)
