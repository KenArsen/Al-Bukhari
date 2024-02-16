from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.event.serializers import EventSerializer
from apps.event.services import (
    EventListService,
    EventRetrieveService,
    EventCreateService,
    EventUpdateService,
    EventDeleteService,
)


class EventListView(views.APIView):
    @swagger_auto_schema(
        responses={200: EventSerializer(many=True)},
        tags=["Event"],
        operation_summary="List events",
        operation_description="Get a list of all events"
    )
    def get(self, request):
        service = EventListService.get_events()
        return Response(service, status=status.HTTP_200_OK)


class EventRetrieveView(views.APIView):
    @swagger_auto_schema(
        responses={200: EventSerializer()},
        tags=["Event"],
        operation_summary="Retrieve an event",
        operation_description="Retrieve detailed information about a specific event"
    )
    def get(self, request, pk=None):
        service = EventRetrieveService.get_event(pk=pk)
        return Response(service, status=status.HTTP_200_OK)


class EventCreateView(views.APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['title', 'organizer', 'email', 'phone', 'more', 'date', 'address', 'images'],
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the event'),
                'organizer': openapi.Schema(type=openapi.TYPE_STRING, description='Organizer of the event'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the event'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Phone of the event'),
                'more': openapi.Schema(type=openapi.TYPE_STRING, description='More of the event'),
                'date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,
                                       description='Date of the event'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, description='Address of the event'),
                'images': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_FILE),
                                        description='Image of the event')
            }
        ),
        responses={201: EventSerializer()},
        tags=['Event'],
        operation_summary="Create an event",
        operation_description="Create a new event with the provided data"
    )
    def post(self, request):
        service, status = EventCreateService.create_event(event=request)
        return Response(service, status=status)


class EventUpdateView(views.APIView):
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['title', 'organizer', 'email', 'phone', 'more', 'date', 'address', 'images'],
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the event'),
                'organizer': openapi.Schema(type=openapi.TYPE_STRING, description='Organizer of the event'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the event'),
                'phone': openapi.Schema(type=openapi.TYPE_STRING, description='Phone of the event'),
                'more': openapi.Schema(type=openapi.TYPE_STRING, description='More of the event'),
                'date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME,
                                       description='Date of the event'),
                'address': openapi.Schema(type=openapi.TYPE_STRING, description='Address of the event'),
                'images': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_FILE),
                                        description='Image of the event')
            }
        ),
        responses={200: EventSerializer()},
        tags=['Event'],
        operation_summary="Update an event",
        operation_description="Update an existing event with the provided data"
    )
    def put(self, request, pk):
        service, status = EventUpdateService.update_event(event_data=request.data, pk=pk)
        return Response(service, status=status)


class EventDeleteView(views.APIView):
    @swagger_auto_schema(
        responses={204: 'No content'},
        tags=["Event"],
        operation_summary="Delete an event",
        operation_description="Delete an existing event"
    )
    def delete(self, request, pk):
        service = EventDeleteService.delete_event(pk)
        return Response(service)
