from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets

from apps.common.permissions import IsAdmin
from apps.image.repositories import ImageRepository
from apps.image.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageRepository.get_images()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        tags=["Images"],
        operation_summary="Retrieve a list of all images",
        operation_description="Returns a list of all images.",
        responses={200: ImageSerializer(many=True)},
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Images"],
        operation_summary="Retrieve details of a specific image",
        operation_description="Returns the details of a specific image.",
        responses={200: ImageSerializer()},
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Images"],
        operation_summary="Create a new image",
        operation_description="Creates a new image.",
        request_body=ImageSerializer,
        responses={201: ImageSerializer()},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Images"],
        operation_summary="Update an existing image",
        operation_description="Updates an existing image.",
        request_body=ImageSerializer,
        responses={200: ImageSerializer()},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Images"],
        operation_summary="Update partial fields of an existing image",
        operation_description="Updates partial fields of an existing image.",
        request_body=ImageSerializer,
        responses={200: ImageSerializer()},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Images"],
        operation_summary="Delete an existing image",
        operation_description="Deletes an existing image.",
        responses={204: "No Content"},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
