from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from apps.education.api.v1.serializers import GhuslAndTaharatSerializer
from apps.education.models import GhuslAndTaharat


class GhuslAndTaharatListAPI(generics.ListAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer

    @swagger_auto_schema(
        responses={200: GhuslAndTaharatSerializer(many=True)},
        tags=["GhuslAndTaharat"],
        operation_summary="List GhuslAndTaharat",
        operation_description="Get a list of all GhuslAndTaharat",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GhuslAndTaharatCreateAPI(generics.CreateAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=GhuslAndTaharatSerializer,
        responses={201: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Create GhuslAndTaharat",
        operation_description="Create a new GhuslAndTaharat with the provided data",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GhuslAndTaharatDetailAPI(generics.RetrieveAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer

    @swagger_auto_schema(
        responses={200: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Retrieve GhuslAndTaharat",
        operation_description="Retrieve detailed information about a specific GhuslAndTaharat",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GhuslAndTaharatUpdateAPI(generics.UpdateAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=GhuslAndTaharatSerializer,
        responses={200: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Update GhuslAndTaharat",
        operation_description="Update an existing GhuslAndTaharat with the provided data",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=GhuslAndTaharatSerializer,
        responses={200: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Partial Update GhuslAndTaharat",
        operation_description="Update some fields of an existing GhuslAndTaharat with the provided data",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class GhuslAndTaharatDeleteAPI(generics.DestroyAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["GhuslAndTaharat"],
        operation_summary="Delete GhuslAndTaharat",
        operation_description="Delete an existing GhuslAndTaharat",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
