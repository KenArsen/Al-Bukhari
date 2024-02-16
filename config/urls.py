from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
    path('api/v1/healthcheck/', HealthCheckView.as_view(), name='healthcheck')
]

if settings.DEBUG:
    # debug toolbar
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
    # silk
    urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

# static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
