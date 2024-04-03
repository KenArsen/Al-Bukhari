from django.urls import path

from apps.service.api.v1.apis import (
    ServiceCreateAPI,
    ServiceDeleteAPI,
    ServiceDetailAPI,
    ServiceListAPI,
    ServiceUpdateAPI,
)

app_name = "service"

urlpatterns = [
    path("", ServiceListAPI.as_view(), name="service-list"),
    path("create/", ServiceCreateAPI.as_view(), name="service"),
    path("<int:pk>/", ServiceDetailAPI.as_view(), name="service-detail"),
    path("<int:pk>/update/", ServiceUpdateAPI.as_view(), name="service-update"),
    path("<int:pk>/delete/", ServiceDeleteAPI.as_view(), name="service-delete"),
]
