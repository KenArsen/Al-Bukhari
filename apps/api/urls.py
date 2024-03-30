from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.common.data_base import (
    DumpDataAPIView,
    ImageDumpDataAPIView,
    ImageLoadDataAPIView,
    LoadDataAPIView,
    ResizeImagesAPI,
)

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
    permission_classes=[permissions.AllowAny],
)

app_name = "api"

urlpatterns = [
    path("v1/users/", include("apps.user.api.v1.urls", namespace="users")),
    path("v1/events/", include("apps.event.api.v1.urls", namespace="events")),
    path("v1/educations/", include("apps.education.api.v1.urls", namespace="educations")),
    path("v1/donations/", include("apps.donation.api.v1.urls", namespace="donations")),
    path("v1/us/", include("apps.us.api.v1.urls", namespace="us")),
]

urlpatterns += [
    path("v1/resize_images/", ResizeImagesAPI.as_view(), name="namaz-resize-images"),
    path("v1/dumpdata/", DumpDataAPIView.as_view(), name="dump-data"),
    path("v1/loaddata/", LoadDataAPIView.as_view(), name="load-data"),
    path("v1/images/dumpdata/", ImageDumpDataAPIView.as_view(), name="images-dump-data"),
    path("v1/images/loaddata/", ImageLoadDataAPIView.as_view(), name="images-load-data"),
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

# token
urlpatterns += [
    path("v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# swagger
urlpatterns += [
    path("swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
