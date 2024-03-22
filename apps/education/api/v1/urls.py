from django.urls import path

from apps.education.api.v1.apis import (
    EducationCreateAPI,
    EducationDeleteAPI,
    EducationDetailAPI,
    EducationListAPI,
    EducationUpdateAPI,
    GhuslAndTaharatCreateAPI,
    GhuslAndTaharatDeleteAPI,
    GhuslAndTaharatDetailAPI,
    GhuslAndTaharatListAPI,
    GhuslAndTaharatUpdateAPI,
    NamazCreateAPI,
    NamazDeleteAPI,
    NamazDetailAPI,
    NamazListAPI,
    NamazUpdateAPI,
    ResizeImagesAPI,
)
from apps.education.api.v1.apis.resize_images_apis import (
    DumpDataAPIView,
    LoadDataAPIView,
)

app_name = "educations"

# educations
urlpatterns = [
    path("", EducationListAPI.as_view(), name="education-list"),
    path("create/", EducationCreateAPI.as_view(), name="education-create"),
    path("<int:pk>/", EducationDetailAPI.as_view(), name="education-detail"),
    path("<int:pk>/update/", EducationUpdateAPI.as_view(), name="education-update"),
    path("<int:pk>/delete/", EducationDeleteAPI.as_view(), name="education-delete"),
]

# GhuslAndTahara
urlpatterns += [
    path("ghusl_and_taharat/", GhuslAndTaharatListAPI.as_view(), name="ghusl_and_taharat-list"),
    path("ghusl_and_taharat/create/", GhuslAndTaharatCreateAPI.as_view(), name="ghusl_and_taharat-create"),
    path("ghusl_and_taharat/<int:pk>/", GhuslAndTaharatDetailAPI.as_view(), name="ghusl_and_taharat-detail"),
    path("ghusl_and_taharat/<int:pk>/update/", GhuslAndTaharatUpdateAPI.as_view(), name="ghusl_and_taharat-update"),
    path("ghusl_and_taharat/<int:pk>/delete/", GhuslAndTaharatDeleteAPI.as_view(), name="ghusl_and_taharat-delete"),
]

# Namaz
urlpatterns += [
    path("namaz/", NamazListAPI.as_view(), name="namaz-list"),
    path("namaz/create/", NamazCreateAPI.as_view(), name="namaz-create"),
    path("namaz/<int:pk>/", NamazDetailAPI.as_view(), name="namaz-detail"),
    path("namaz/<int:pk>/update/", NamazUpdateAPI.as_view(), name="namaz-update"),
    path("namaz/<int:pk>/delete/", NamazDeleteAPI.as_view(), name="namaz-delete"),
    path("namaz/resize_images/", ResizeImagesAPI.as_view(), name="namaz-resize-images"),
    path("namaz/dumpdata/", DumpDataAPIView.as_view(), name="dump-data"),
    path("namaz/loaddata/", LoadDataAPIView.as_view(), name="load-data"),
]
