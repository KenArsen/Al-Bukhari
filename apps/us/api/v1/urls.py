from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.us.api.v1.apis import (
    AboutCreateAPI,
    AboutDeleteAPI,
    AboutDetailAPI,
    AboutListAPI,
    AboutUpdateAPI,
    ContactCreateAPI,
    ContactDeleteAPI,
    ContactDetailAPI,
    ContactListAPI,
    ContactUpdateAPI,
    UrlVewSet,
)

app_name = "us"

router = DefaultRouter()
router.register(r"url", UrlVewSet)

# about
urlpatterns = [
    path("abouts/", AboutListAPI.as_view(), name="about-list"),
    path("abouts/create/", AboutCreateAPI.as_view(), name="about-create"),
    path("abouts/<int:pk>/", AboutDetailAPI.as_view(), name="about-detail"),
    path("abouts/<int:pk>/update/", AboutUpdateAPI.as_view(), name="about-update"),
    path("abouts/<int:pk>/delete/", AboutDeleteAPI.as_view(), name="about-delete"),
]

# contact
urlpatterns += [
    path("contacts/", ContactListAPI.as_view(), name="contact-list"),
    path("contacts/create/", ContactCreateAPI.as_view(), name="contact-create"),
    path("contacts/<int:pk>/", ContactDetailAPI.as_view(), name="contact-detail"),
    path("contacts/<int:pk>/update/", ContactUpdateAPI.as_view(), name="contact-update"),
    path("contacts/<int:pk>/delete/", ContactDeleteAPI.as_view(), name="contact-delete"),
]

urlpatterns += router.urls
