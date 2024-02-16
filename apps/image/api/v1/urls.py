from rest_framework import routers
from django.urls import path, include
from apps.image.apis import ImageViewSet

router = routers.DefaultRouter()

router.register(r'', ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
