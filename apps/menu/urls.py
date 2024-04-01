from django.urls import path

from .views import (
    MenuCreateAPI,
    MenuDeleteAPI,
    MenuDetailAPI,
    MenuListAPI,
    MenuUpdateAPI,
)

app_name = "menus"

urlpatterns = [
    path("", MenuListAPI.as_view(), name="menu-list"),
    path("create/", MenuCreateAPI.as_view(), name="menu-create"),
    path("<int:pk>/", MenuDetailAPI.as_view(), name="menu-detail"),
    path("<int:pk>/update/", MenuUpdateAPI.as_view(), name="menu-update"),
    path("<int:pk>/delete/", MenuDeleteAPI.as_view(), name="menu-delete"),
]
