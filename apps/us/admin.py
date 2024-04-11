from django.contrib import admin

from apps.us.models import About, Contact, Url

admin.site.register(About)
admin.site.register(Contact)


@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type_url')
    list_display_links = ('id', 'title')
