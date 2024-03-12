from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

from apps.us.api.v1.serializers import AboutUsSerializer
from apps.us.models import About


class AboutListAPI(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer

    @swagger_auto_schema(
        responses={200: AboutUsSerializer(many=True)},
        tags=["About"],
        operation_summary="List About",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AboutDetailAPI(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer

    @swagger_auto_schema(
        responses={200: AboutUsSerializer()},
        tags=["About"],
        operation_summary="Retrieve an About",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AboutCreateAPI(generics.CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer

    @swagger_auto_schema(
        request_body=AboutUsSerializer,
        responses={201: AboutUsSerializer()},
        tags=["About"],
        operation_summary="Create an About",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AboutUpdateAPI(generics.UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer

    @swagger_auto_schema(
        request_body=AboutUsSerializer,
        responses={200: AboutUsSerializer()},
        tags=["About"],
        operation_summary="Update an About",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=AboutUsSerializer,
        responses={200: AboutUsSerializer()},
        tags=["About"],
        operation_summary="Update an About",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AboutDeleteAPI(generics.DestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["About"],
        operation_summary="Delete an About",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
