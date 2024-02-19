from django.urls import path
from apps.event import apis

urlpatterns = [
    path('', apis.EventListView.as_view(), name='event-list'),
    path('create/', apis.EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', apis.EventRetrieveView.as_view(), name='event-detail'),
    path('<int:pk>/update/', apis.EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete/', apis.EventDeleteView.as_view(), name='event-delete'),
]
