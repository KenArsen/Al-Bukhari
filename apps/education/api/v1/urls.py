from django.urls import path

from apps.education.api.v1.apis import (
    EducationCreateAPI,
    EducationDeleteAPI,
    EducationDetailAPI,
    EducationListAPI,
    EducationListCreateAPI,
    EducationListDeleteAPI,
    EducationListDetailAPI,
    EducationListListAPI,
    EducationListUpdateAPI,
    EducationUpdateAPI,
    GhuslCreateAPI,
    GhuslDeleteAPI,
    GhuslDetailAPI,
    GhuslListAPI,
    GhuslUpdateAPI,
    NamazCreateAPI,
    NamazDeleteAPI,
    NamazDetailAPI,
    NamazListAPI,
    NamazUpdateAPI,
    TaharatCreateAPI,
    TaharatDeleteAPI,
    TaharatDetailAPI,
    TaharatListAPI,
    TaharatUpdateAPI,
)

app_name = "education"

# educations
urlpatterns = [
    path("", EducationListAPI.as_view(), name="education-list"),
    path("create/", EducationCreateAPI.as_view(), name="education-create"),
    path("<int:pk>/", EducationDetailAPI.as_view(), name="education-detail"),
    path("<int:pk>/update/", EducationUpdateAPI.as_view(), name="education-update"),
    path("<int:pk>/delete/", EducationDeleteAPI.as_view(), name="education-delete"),
]

# education_list
urlpatterns += [
    path("list/", EducationListListAPI.as_view(), name="education_list-list"),
    path("list/create/", EducationListCreateAPI.as_view(), name="education_list-create"),
    path("list/<int:pk>/", EducationListDetailAPI.as_view(), name="education_list-detail"),
    path("list/<int:pk>/update/", EducationListUpdateAPI.as_view(), name="education_list-update"),
    path("list/<int:pk>/delete/", EducationListDeleteAPI.as_view(), name="education_list-delete"),
]

# Ghusl
urlpatterns += [
    path("ghusl/", GhuslListAPI.as_view(), name="ghusl-list"),
    path("ghusl/create/", GhuslCreateAPI.as_view(), name="ghusl-create"),
    path("ghusl/<int:pk>/", GhuslDetailAPI.as_view(), name="ghusl-detail"),
    path("ghusl/<int:pk>/update/", GhuslUpdateAPI.as_view(), name="ghusl-update"),
    path("ghusl/<int:pk>/delete/", GhuslDeleteAPI.as_view(), name="ghusl-delete"),
]

# Taharat
urlpatterns += [
    path("taharat/", TaharatListAPI.as_view(), name="taharat-list"),
    path("taharat/create/", TaharatCreateAPI.as_view(), name="taharat-create"),
    path("taharat/<int:pk>/", TaharatDetailAPI.as_view(), name="taharat-detail"),
    path("taharat/<int:pk>/update/", TaharatUpdateAPI.as_view(), name="taharat-update"),
    path("taharat/<int:pk>/delete/", TaharatDeleteAPI.as_view(), name="taharat-delete"),
]

# Namaz
urlpatterns += [
    path("namaz/", NamazListAPI.as_view(), name="namaz-list"),
    path("namaz/create/", NamazCreateAPI.as_view(), name="namaz-create"),
    path("namaz/<int:pk>/", NamazDetailAPI.as_view(), name="namaz-detail"),
    path("namaz/<int:pk>/update/", NamazUpdateAPI.as_view(), name="namaz-update"),
    path("namaz/<int:pk>/delete/", NamazDeleteAPI.as_view(), name="namaz-delete"),
]
