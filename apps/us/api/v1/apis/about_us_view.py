from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.response import Response

from apps.us.api.v1.serializers.about_serializer import AboutUsSerializer
from apps.us.api.v1.services.about_services import (
    AboutCreateService,
    AboutDeleteService,
    AboutListService,
    AboutRetrieveService,
    AboutUpdateService,
)


class AboutListView(views.APIView):
    @swagger_auto_schema(
        responses={200: AboutUsSerializer(many=True)},
        tags=["About us"],
        operation_summary="List About us",
        operation_description="Get a list of all About",
    )
    def get(
        self,
        request,
    ):
        about = AboutListService.get_about()
        return Response(about, status=status.HTTP_200_OK)


class AboutRetrieveView(views.APIView):
    @swagger_auto_schema(
        responses={200: AboutUsSerializer(many=True)},
        tags=["About us"],
        operation_summary="Retrieve an About us",
        operation_description="Retrieve detailed information about a specific about us",
    )
    def get(self, request, pk=None):
        about = AboutRetrieveService.get_about(pk=pk)
        return Response(about, status=status.HTTP_200_OK)


class AboutCreateView(views.APIView):
    @swagger_auto_schema(
        responses={200: AboutUsSerializer(many=True)},
        tags=["Abot us"],
        operation_summary="Create an About us",
        operation_description="Create information about a specific about us",
    )
    def post(self, request):
        about = AboutCreateService.create_about(data=request.data)
        return Response(about)


class AboutUpdateView(views.APIView):
    @swagger_auto_schema(
        responses={200: AboutUsSerializer(many=True)},
        tags=["About us"],
        operation_summary="Update an About us",
        operation_description="Update an existing About us with the provided data",
    )
    def put(self, request, pk):
        about = AboutUpdateService.update_about(about_data=request.data, pk=pk)
        return Response(about)


class AboutDeleteView(views.APIView):
    # permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["About us"],
        operation_summary="Delete an About us",
        operation_description="Delete an existing About us",
    )
    def delete(self, request, pk):
        service = AboutDeleteService.delete_about(pk)
        return Response(service)
