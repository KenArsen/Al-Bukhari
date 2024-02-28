from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    authentication_classes=[SessionAuthentication],
    permission_classes=[permissions.IsAuthenticated],
)

app_name = "api"

urlpatterns = [
    path("v1/events/", include("apps.event.api.v1.urls", namespace="events")),
    path("v1/images/", include("apps.image.api.v1.urls", namespace="images")),
    path("v1/educations/", include("apps.education.api.v1.urls", namespace="educations")),
]

# libraries
urlpatterns += [
    re_path(
        r"^static/(?P<path>.*)$",
        serve,
        {"document_root": settings.STATIC_ROOT, "show_indexes": settings.DEBUG},
    ),
    re_path(
        r"^api/v1/media/(?P<path>.*)$",
        serve,
        {"document_root": settings.MEDIA_ROOT, "show_indexes": settings.DEBUG},
    ),
]

# swagger
urlpatterns += [
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
