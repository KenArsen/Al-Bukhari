from django.urls import path
from apps.event import apis

urlpatterns = [
<<<<<<< HEAD
    path('', apis.EventListView.as_view(), name='event-list'),
    path('create/', apis.EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/', apis.EventRetrieveView.as_view(), name='event-detail'),
    path('<int:pk>/update/', apis.EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete/', apis.EventDeleteView.as_view(), name='event-delete'),
=======
    path("", apis.EventListView.as_view(), name="event-list"),
    path("create/", apis.EventCreateView.as_view(), name="event-create"),
    path("<int:pk>/", apis.EventRetrieveView.as_view(), name="event-detail"),
    path("<int:pk>/update/", apis.EventUpdateView.as_view(), name="event-update"),
    path("<int:pk>/delete/", apis.EventDeleteView.as_view(), name="event-delete"),
>>>>>>> 24677ec (added STATICFILES_DIRS)
]
