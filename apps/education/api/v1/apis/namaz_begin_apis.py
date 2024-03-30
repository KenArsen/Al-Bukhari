from rest_framework import generics, exceptions
from drf_yasg.utils import swagger_auto_schema

from apps.education.models import NamazBegin
from apps.education.api.v1.serializers import NamazBeginSerializer


class NamazBeginListAPI(generics.ListAPIView):
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="List Namaz Begin",
    )
    def get_queryset(self):
        queryset = NamazBegin.objects.all()
        namaz_type = self.request.data.get("namaz_type", None)
        gender = self.request.data.get("gender", None)

        if namaz_type and gender:
            return queryset.filter(namaz_type=namaz_type, gender=gender)
        elif namaz_type and gender is None:
            return queryset.filter(namaz_type=namaz_type)
        elif gender and namaz_type is None:
            raise exceptions.ValidationError({"error": "namaz_type parameter is required"})
        else:
            return queryset


class NamazBeginDetailAPI(generics.RetrieveAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="Retrieve Namaz Begin",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NamazBeginCreateAPI(generics.CreateAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="Create Namaz Begin",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NamazBeginUpdateAPI(generics.UpdateAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer(many=True)},
        tags=["Namaz Begin"],
        operation_summary="Update Namaz Begin",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={200: NamazBeginSerializer()},
        tags=["Namaz Begin"],
        operation_summary="Update Namaz Begin",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class NamazBeginDeleteAPI(generics.DestroyAPIView):
    queryset = NamazBegin.objects.all()
    serializer_class = NamazBeginSerializer

    @swagger_auto_schema(tags=["Namaz Begin"])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
