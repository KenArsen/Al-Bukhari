from django.urls import path

from apps.us.api.v1.apis.about_us_view import (
    AboutCreateView,
    AboutDeleteView,
    AboutListView,
    AboutRetrieveView,
    AboutUpdateView,
)

app_name = "about_us"

urlpatterns = [
    path("", AboutListView.as_view(), name="about-list"),
    path("create/", AboutCreateView.as_view(), name="about-create"),
    path("<int:pk>/", AboutRetrieveView.as_view(), name="about-detail"),
    path("<int:pk>/update", AboutUpdateView.as_view(), name="about-update"),
    path("<int:pk>/delete", AboutDeleteView.as_view(), name="about-delete"),
]
