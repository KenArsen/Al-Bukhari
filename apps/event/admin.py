from django.contrib import admin

from apps.event.models import Event, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("title",)
    fields = ("title", "organizer", "email", "phone", "more", "date", "address")
    readonly_fields = ("created_at", "updated_at")
    inlines = [EventImageInline]
