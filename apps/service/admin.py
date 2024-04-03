from django.contrib import admin

from apps.service.models import Service, ServiceImage

admin.site.register(Service)
admin.site.register(ServiceImage)
