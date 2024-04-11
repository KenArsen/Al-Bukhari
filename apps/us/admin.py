from django.contrib import admin

from apps.us.models import About, Contact, Url

admin.site.register(About)


class UrlInline(admin.TabularInline):
    model = Url
    extra = 1


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [UrlInline]


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type_url')
    list_display_links = ('id', 'title')
