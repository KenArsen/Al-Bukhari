from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from apps.common.permissions import IsSuperAdmin
from apps.event.api.v1.serializers import EventSerializer
from apps.event.models import Event
from apps.event.repositories import EventRepository
from apps.image.services import ImageService


class EventListAPI(generics.ListAPIView):
    queryset = EventRepository.get_all()
    serializer_class = EventSerializer

    @swagger_auto_schema(
        responses={200: EventSerializer(many=True)},
        tags=["Event"],
        operation_summary="List events",
        operation_description="Get a list of all events",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EventCreateAPI(generics.CreateAPIView):
    queryset = EventRepository.get_all()
    serializer_class = EventSerializer
    service = ImageService(serializer=EventSerializer)
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "organizer", "email", "phone", "more", "date", "address", "images"],
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="Title of the event"),
                "organizer": openapi.Schema(type=openapi.TYPE_STRING, description="Organizer of the event"),
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email of the event"),
                "phone": openapi.Schema(type=openapi.TYPE_STRING, description="Phone of the event"),
                "more": openapi.Schema(type=openapi.TYPE_STRING, description="More of the event"),
                "date": openapi.Schema(
                    type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description="Date of the event"
                ),
                "address": openapi.Schema(type=openapi.TYPE_STRING, description="Address of the event"),
                "images": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_FILE),
                    description="Image of the event",
                ),
            },
        ),
        responses={201: EventSerializer()},
        tags=["Event"],
        operation_summary="Create an event",
        operation_description="Create a new event with the provided data",
    )
    def post(self, request, *args, **kwargs):
        serializer = self.service.create_image(request=request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class EventRetrieveAPI(generics.RetrieveAPIView):
    queryset = EventRepository.get_all()
    serializer_class = EventSerializer

    @swagger_auto_schema(
        responses={200: EventSerializer()},
        tags=["Event"],
        operation_summary="Retrieve an event",
        operation_description="Retrieve detailed information about a specific event",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EventUpdateAPI(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    service = ImageService(serializer=EventSerializer, repository=EventRepository)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["title", "organizer", "email", "phone", "more", "date", "address", "images"],
            properties={
                "title": openapi.Schema(type=openapi.TYPE_STRING, description="Title of the event"),
                "organizer": openapi.Schema(type=openapi.TYPE_STRING, description="Organizer of the event"),
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email of the event"),
                "phone": openapi.Schema(type=openapi.TYPE_STRING, description="Phone of the event"),
                "more": openapi.Schema(type=openapi.TYPE_STRING, description="More of the event"),
                "date": openapi.Schema(
                    type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description="Date of the event"
                ),
                "address": openapi.Schema(type=openapi.TYPE_STRING, description="Address of the event"),
                "images": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_FILE),
                    description="Image of the event",
                ),
            },
        ),
        responses={200: EventSerializer()},
        tags=["Event"],
        operation_summary="Update an event",
        operation_description="Update an existing event with the provided data",
    )
    def put(self, request, pk):
        serializer = self.service.update_image(request=request, pk=pk)
        return Response(serializer.data)


class EventDeleteAPI(generics.DestroyAPIView):
    queryset = EventRepository.get_all()
    service = ImageService(repository=EventRepository, obj=Event)
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Event"],
        operation_summary="Delete an event",
        operation_description="Delete an existing event",
    )
    def delete(self, request, *args, **kwargs):
        self.service.delete_image(pk=kwargs.get("pk"))
        return self.destroy(request, *args, **kwargs)
