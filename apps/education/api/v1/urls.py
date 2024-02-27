from django.urls import path, include
from rest_framework import routers
from apps.education.api.v1.apis.education_api import (
    EducationListAPI,
    EducationDetailAPI,
    EducationCreateAPI,
    EducationUpdateAPI,
    EducationDeleteAPI,
)

from apps.education.api.v1.apis.namaz_api import (
    GhuslAndTaharatViewSet,
    NamazViewSet,
)

app_name = "educations"

router = routers.DefaultRouter()
router.register(r"namaz", NamazViewSet)
router.register(r"ghusl_and_taharat", GhuslAndTaharatViewSet)

urlpatterns = [
    path("", EducationListAPI.as_view(), name="education-list"),
    path("create/", EducationCreateAPI.as_view(), name="education-create"),
    path("<int:pk>/", EducationDetailAPI.as_view(), name="education-detail"),
    path("<int:pk>/update/", EducationUpdateAPI.as_view(), name="education-update"),
    path("<int:pk>/delete/", EducationDeleteAPI.as_view(), name="education-delete"),
]

urlpatterns += router.urls
