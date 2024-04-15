from django.contrib import admin

from apps.education.models.education_model import Education, EducationCategory
from apps.education.models.namaz_model import Ghusl, Namaz, NamazImage, Taharat

admin.site.register(Ghusl)
admin.site.register(Taharat)
admin.site.register(EducationCategory)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("id", "category")


class NamazImageInline(admin.TabularInline):
    model = NamazImage
    extra = 1


@admin.register(NamazImage)
class NamazImageAdmin(admin.ModelAdmin):
    list_display = ("id", "namaz", "image")


@admin.register(Namaz)
class NamazAdmin(admin.ModelAdmin):
    list_display = ("id", "namaz_type", "gender", "namaz_number", "prayer_part1")
    list_display_links = ("id", "namaz_type")
    inlines = [NamazImageInline]
