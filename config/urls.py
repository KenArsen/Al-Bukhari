from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("ckeditor5/", include("django_ckeditor_5.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls", namespace="api")),
]

if settings.DEBUG:
    # debug toolbar
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    # silk
    urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]
    # static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
