from django.urls import path

from apps.event.api.v1.apis import (
    EventCreateAPI,
    EventDeleteAPI,
    EventListAPI,
    EventRetrieveAPI,
    EventUpdateAPI,
)

app_name = "events"

urlpatterns = [
    path("", EventListAPI.as_view(), name="event-list"),
    path("create/", EventCreateAPI.as_view(), name="event-create"),
    path("<int:pk>/", EventRetrieveAPI.as_view(), name="event-detail"),
    path("<int:pk>/update/", EventUpdateAPI.as_view(), name="event-update"),
    path("<int:pk>/delete/", EventDeleteAPI.as_view(), name="event-delete"),
]
