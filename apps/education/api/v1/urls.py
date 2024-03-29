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

    NamazBeginListAPI,
    NamazBeginCreateAPI,
    NamazBeginDetailAPI,
    NamazBeginUpdateAPI,
    NamazBeginDeleteAPI,
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

# Namaz begin
urlpatterns = [
    path("namaz_begin/", NamazBeginListAPI.as_view(), name="namaz_begin-list"),
    path("namaz_begin/create/", NamazBeginCreateAPI.as_view(), name="namaz_begin-create"),
    path("namaz_begin/<int:pk>/", NamazBeginDetailAPI.as_view(), name="namaz_begin-detail"),
    path("namaz_begin/<int:pk>/update/", NamazBeginUpdateAPI.as_view(), name="namaz_begin-update"),
    path("namaz_begin/<int:pk>/delete/", NamazBeginDeleteAPI.as_view(), name="namaz_begin-delete")
]

# Namaz
urlpatterns += [
    path("namaz/", NamazListAPI.as_view(), name="namaz-list"),
    path("namaz/create/", NamazCreateAPI.as_view(), name="namaz-create"),
    path("namaz/<int:pk>/", NamazDetailAPI.as_view(), name="namaz-detail"),
    path("namaz/<int:pk>/update/", NamazUpdateAPI.as_view(), name="namaz-update"),
    path("namaz/<int:pk>/delete/", NamazDeleteAPI.as_view(), name="namaz-delete"),
]
