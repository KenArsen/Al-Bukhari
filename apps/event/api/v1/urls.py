from django.urls import path

from apps.event.api.v1.apis import (
    EventCreateView,
    EventDeleteView,
    EventListView,
    EventRetrieveView,
    EventUpdateView,
)

app_name = "events"

urlpatterns = [
    path("", EventListView.as_view(), name="event-list"),
    path("create/", EventCreateView.as_view(), name="event-create"),
    path("<int:pk>/", EventRetrieveView.as_view(), name="event-detail"),
    path("<int:pk>/update/", EventUpdateView.as_view(), name="event-update"),
    path("<int:pk>/delete/", EventDeleteView.as_view(), name="event-delete"),
]
