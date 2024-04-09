from django.urls import path
from .apis import (
    FaqListAPI,
    FaqCreateAPI,
    FaqDetailAPI,
    FaqUpdateAPI,
    FaqDeleteAPI,
)

app_name = 'faq'

urlpatterns = [
    path("", FaqListAPI.as_view(), name="faq-list"),
    path("create/", FaqCreateAPI.as_view(), name="faq-create"),
    path("<int:pk>/", FaqDetailAPI.as_view(), name="faq-detail"),
    path("<int:pk>/update/", FaqUpdateAPI.as_view(), name="faq-update"),
    path("<int:pk>/delete/", FaqDeleteAPI.as_view(), name="faq-delete"),
]
