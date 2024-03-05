from django.contrib import admin

from .models import Customer, Donate

admin.site.register(Donate)
admin.site.register(Customer)
