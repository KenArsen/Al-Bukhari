from django.contrib import admin
from apps.education.models.education_model import Education
from apps.education.models.namaz_model import GhuslAndTaharat, Namaz

admin.site.register(Education)
admin.site.register(GhuslAndTaharat)
admin.site.register(Namaz)
