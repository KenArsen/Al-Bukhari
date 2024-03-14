from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from apps.common import IsSuperAdmin
from apps.education.api.v1.serializers import NamazSerializer
from apps.education.models import Namaz
from apps.education.repositories import NamazRepository
from apps.image.services import ImageService


class NamazListAPI(generics.ListAPIView):
    queryset = NamazRepository().get_all()
    serializer_class = NamazSerializer

    @swagger_auto_schema(
        responses={200: NamazSerializer(many=True)},
        tags=["Namaz"],
        operation_summary="List Namaz",
        operation_description="Get a list of all Namaz",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NamazCreateAPI(generics.CreateAPIView):
    queryset = NamazRepository().get_all()
    serializer_class = NamazSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    service = ImageService(serializer=NamazSerializer)

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={201: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Create Namaz",
        operation_description="Create a new Namaz with the provided data",
    )
    def post(self, request, *args, **kwargs):
        serializer = self.service.create_image(request=request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class NamazDetailAPI(generics.RetrieveAPIView):
    queryset = NamazRepository().get_all()
    serializer_class = NamazSerializer

    @swagger_auto_schema(
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Retrieve Namaz",
        operation_description="Retrieve detailed information about a specific Namaz",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NamazUpdateAPI(generics.UpdateAPIView):
    queryset = NamazRepository().get_all()
    serializer_class = NamazSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    service = ImageService(serializer=NamazSerializer, repository=NamazRepository)

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Update Namaz",
        operation_description="Update an existing Namaz with the provided data",
    )
    def put(self, request, *args, **kwargs):
        serializer = self.service.update_image(request=request, pk=kwargs.get("pk"))
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Partial Update Namaz",
        operation_description="Update some fields of an existing Namaz with the provided data",
    )
    def patch(self, request, *args, **kwargs):
        serializer = self.service.update_image(request=request, pk=kwargs.get("pk"))
        return Response(serializer.data)


class NamazDeleteAPI(generics.DestroyAPIView):
    queryset = NamazRepository().get_all()
    serializer_class = NamazSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    service = ImageService(repository=NamazRepository, obj=Namaz)

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Namaz"],
        operation_summary="Delete Namaz",
        operation_description="Delete an existing Namaz",
    )
    def delete(self, request, *args, **kwargs):
        self.service.delete_image(pk=kwargs.get("pk"))
        return self.destroy(request, *args, **kwargs)
