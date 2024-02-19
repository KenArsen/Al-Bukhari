from django.urls import include, path
from rest_framework import routers

from apps.image import apis

router = routers.DefaultRouter()

router.register(r"", apis.ImageViewSet)

urlpatterns = [path("", include(router.urls))]
