from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from apps.education.api.v1.serializers import GhuslAndTaharatSerializer, NamazSerializer
from apps.education.models import GhuslAndTaharat, Namaz


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

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["GhuslAndTaharat"],
        operation_summary="Delete GhuslAndTaharat",
        operation_description="Delete an existing GhuslAndTaharat",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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
    serializer_class = NamazSerializer

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={201: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Create Namaz",
        operation_description="Create a new Namaz with the provided data",
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
        operation_description="Retrieve detailed information about a specific Namaz",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NamazUpdateAPI(generics.UpdateAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazSerializer

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Update Namaz",
        operation_description="Update an existing Namaz with the provided data",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=NamazSerializer,
        responses={200: NamazSerializer()},
        tags=["Namaz"],
        operation_summary="Partial Update Namaz",
        operation_description="Update some fields of an existing Namaz with the provided data",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class NamazDeleteAPI(generics.DestroyAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazSerializer

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Namaz"],
        operation_summary="Delete Namaz",
        operation_description="Delete an existing Namaz",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
