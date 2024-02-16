from django.contrib import admin
from apps.image.models import Image
from apps.event.models import Event


class EventInline(admin.TabularInline):
    model = Event.images.through
    extra = 1


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    inlines = [EventInline]
