from rest_framework import routers
from django.urls import path, include
from apps.image import apis

router = routers.DefaultRouter()

router.register(r'', apis.ImageViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = [
#     path('', apis.ImageListView.as_view(), name='image-list'),
#     path('create/', apis.ImageCreateView.as_view(), name='image-create'),
#     path('<int:pk>/', apis.ImageDetailView.as_view(), name='image-detail'),
#     path('<int:pk>/update/', apis.ImageUpdateView.as_view(), name='image-update'),
#     path('<int:pk>/delete/', apis.ImageDeleteView.as_view(), name='image-delete'),
# ]
