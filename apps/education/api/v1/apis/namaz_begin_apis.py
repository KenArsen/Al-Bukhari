from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema

from apps.education.models import NamazBegin
from apps.education.api.v1.serializers import NamazBeginSerializer


class NamazBeginListAPI(generics.ListAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="List Namaz",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NamazBeginDetailAPI(generics.RetrieveAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="Retrieve Namaz",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NamazBeginCreateAPI(generics.CreateAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="Create Namaz",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NamazBeginUpdateAPI(generics.UpdateAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="Update Namaz",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer()},
        tags=["Namaz Begin"],
        operation_summary="Update Namaz",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class NamazBeginDeleteAPI(generics.DestroyAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(tags=["Namaz Begin"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
