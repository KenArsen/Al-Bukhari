from django.contrib import admin

from apps.event.models import Event
from apps.image.models import Image


class EventInline(admin.TabularInline):
    model = Event.images.through
    extra = 1


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    inlines = [EventInline]
