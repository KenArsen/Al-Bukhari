from django.contrib import admin

from apps.education.models.education_model import Education
from apps.education.models.namaz_model import GhuslAndTaharat, Namaz, NamazImage, NamazBegin

admin.site.register(Education)
admin.site.register(GhuslAndTaharat)


@admin.register(NamazBegin)
class NamazBeginAdmin(admin.ModelAdmin):
    list_display = ("id", "namaz_type", "gender")
    list_display_links = ("id", "namaz_type")


class NamazImageInline(admin.TabularInline):
    model = NamazImage
    extra = 1


@admin.register(NamazImage)
class NamazImageAdmin(admin.ModelAdmin):
    list_display = ("id", "namaz", "image")


@admin.register(Namaz)
class NamazAdmin(admin.ModelAdmin):
    list_display = ("id", "namaz_type", "gender", "prayer_part1")
    list_display_links = ("id", "namaz_type")
    inlines = [NamazImageInline]
