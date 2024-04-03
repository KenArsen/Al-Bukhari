from django.conf import settings
from django.urls import include, path, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, response, status, views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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


class HealthCheckView(views.APIView):
    def get(self, request, *args, **kwargs):
        return response.Response({"status": "ok"}, status=status.HTTP_200_OK)


urlpatterns = [
    path("v1/healthcheck/", HealthCheckView.as_view(), name="healthcheck"),
    path("v1/us/", include("apps.us.api.v1.urls", namespace="us")),
    path("v1/menus/", include("apps.menu.urls", namespace="menu")),
    path("v1/users/", include("apps.user.api.v1.urls", namespace="user")),
    path("v1/events/", include("apps.event.api.v1.urls", namespace="event")),
    path("v1/services/", include("apps.service.api.v1.urls", namespace="service")),
    path("v1/donations/", include("apps.donation.api.v1.urls", namespace="donation")),
    path("v1/educations/", include("apps.education.api.v1.urls", namespace="education")),
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
