from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions

from apps.common.permissions import IsSuperAdmin
from apps.event.api.v1.serializers import EventCreateUpdateSerializer, EventSerializer
from apps.event.models import Event


class EventListAPI(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @swagger_auto_schema(
        responses={200: EventSerializer(many=True)},
        tags=["Event"],
        operation_summary="List events",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EventCreateAPI(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=EventCreateUpdateSerializer,
        responses={201: EventCreateUpdateSerializer()},
        tags=["Event"],
        operation_summary="Create an event",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EventRetrieveAPI(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @swagger_auto_schema(
        responses={200: EventSerializer()},
        tags=["Event"],
        operation_summary="Retrieve an event",
        operation_description="Retrieve detailed information about a specific event",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EventUpdateAPI(generics.UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=EventCreateUpdateSerializer,
        responses={200: EventCreateUpdateSerializer()},
        tags=["Event"],
        operation_summary="Update an event",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=EventCreateUpdateSerializer,
        responses={200: EventCreateUpdateSerializer()},
        tags=["Event"],
        operation_summary="Update an event",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EventDeleteAPI(generics.DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Event"],
        operation_summary="Delete an event",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
