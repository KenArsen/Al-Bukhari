from rest_framework import viewsets
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from apps.education.models.namaz_model import GhuslAndTaharat, Namaz
from apps.education.api.v1.serializers.namaz_serializer import (
    GhuslAndTaharatSerializer,
    NamazSerializer,
)


class GhuslAndTaharatViewSet(viewsets.ModelViewSet):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer

    @swagger_auto_schema(
        responses={200: GhuslAndTaharatSerializer(many=True)},
        tags=["GhuslAndTaharat"],
        operation_summary="List GhuslAndTaharat",
        operation_description="Get a list of all GhuslAndTaharat",
    )
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={200: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Retrieve GhuslAndTaharat",
        operation_description="Retrieve detailed information about a specific GhuslAndTaharat",
    )
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=GhuslAndTaharatSerializer,
        responses={201: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Create GhuslAndTaharat",
        operation_description="Create a new GhuslAndTaharat with the provided data",
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @swagger_auto_schema(
        request_body=GhuslAndTaharatSerializer,
        responses={200: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Update GhuslAndTaharat",
        operation_description="Update an existing GhuslAndTaharat with the provided data",
    )
    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=GhuslAndTaharatSerializer,
        responses={200: GhuslAndTaharatSerializer()},
        tags=["GhuslAndTaharat"],
        operation_summary="Partial Update GhuslAndTaharat",
        operation_description="Update some fields of an existing GhuslAndTaharat with the provided data",
    )
    def partial_update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["GhuslAndTaharat"],
        operation_summary="Delete GhuslAndTaharat",
        operation_description="Delete an existing GhuslAndTaharat",
    )
    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)


class NamazViewSet(viewsets.ModelViewSet):
    queryset = Namaz.objects.all()
    serializer_class = NamazSerializer

    @swagger_auto_schema(
        responses={200: NamazSerializer(many=True)},
        tags=["Namaz"],
        operation_summary="List Namaz",
        operation_description="Get a list of all Namaz",
    )
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Retrieve Namaz",
        operation_description="Retrieve detailed information about a specific Namaz",
    )
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={201: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Create Namaz",
        operation_description="Create a new Namaz with the provided data",
    )
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Update Namaz",
        operation_description="Update an existing Namaz with the provided data",
    )
    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Partial Update Namaz",
        operation_description="Update some fields of an existing Namaz with the provided data",
    )
    def partial_update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Namaz"],
        operation_summary="Delete Namaz",
        operation_description="Delete an existing Namaz",
    )
    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=204)
