from django.contrib import admin

from apps.event.models import Event


class ImageInline(admin.TabularInline):
    model = Event.images.through
    extra = 1


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
<<<<<<< HEAD
    list_display = ('id', 'title')
    list_display_links = ('title',)
    fields = ('title', 'organizer', 'email', 'phone', 'more', 'date', 'address')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [ImageInline]
    filter_horizontal = ('images',)
=======
    list_display = ("id", "title")
    list_display_links = ("title",)
    fields = ("title", "organizer", "email", "phone", "more", "date", "address")
    readonly_fields = ("created_at", "updated_at")
    inlines = [ImageInline]
    filter_horizontal = ("images",)
>>>>>>> 24677ec (added STATICFILES_DIRS)
