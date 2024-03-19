from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from apps.education.api.v1.serializers import (
    NamazCreateUpdateSerializer,
    NamazSerializer,
)
from apps.education.models import Namaz


class NamazListAPI(generics.ListAPIView):
    queryset = Namaz.objects.all()
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
    queryset = Namaz.objects.all()
    serializer_class = NamazCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=NamazCreateUpdateSerializer,
        responses={201: NamazCreateUpdateSerializer()},
        tags=["Namaz"],
        operation_summary="Create Namaz",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NamazDetailAPI(generics.RetrieveAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazSerializer

    @swagger_auto_schema(
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Retrieve Namaz",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NamazUpdateAPI(generics.UpdateAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazCreateUpdateSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=NamazCreateUpdateSerializer,
        responses={200: NamazCreateUpdateSerializer()},
        tags=["Namaz"],
        operation_summary="Update Namaz",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=NamazCreateUpdateSerializer,
        responses={200: NamazCreateUpdateSerializer()},
        tags=["Namaz"],
        operation_summary="Partial Update Namaz",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class NamazDeleteAPI(generics.DestroyAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Namaz"],
        operation_summary="Delete Namaz",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
