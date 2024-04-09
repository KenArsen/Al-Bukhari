from django.contrib import admin

from apps.education.models.education_model import Education, EducationList
from apps.education.models.namaz_model import Ghusl, Namaz, NamazImage, Taharat


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


@admin.register(EducationList)
class EducationListAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Ghusl)
class GhuslAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Taharat)
class TaharatAdmin(admin.ModelAdmin):
    list_display = ('id',)


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
