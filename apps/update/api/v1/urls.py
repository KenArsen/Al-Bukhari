from django.urls import path
from apps.update.api.v1.apis import (
    UpdateListAPI,
    UpdateDetailAPI,
    CreateUpdateAPI,
    UpdateUpdateAPI,
    DeleteUpdateAPI
)

app_name = 'update'

urlpatterns = [
    path('', UpdateListAPI.as_view(), name='update-list'),
    path('create/', CreateUpdateAPI.as_view(), name='update-create'),
    path('<int:pk>/', UpdateDetailAPI.as_view(), name='update-detail'),
    path('<int:pk>/update/', UpdateUpdateAPI.as_view(), name='update-update'),
    path('<int:pk>/delete/', DeleteUpdateAPI.as_view(), name='update-delete'),
]
