from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions

from apps.common.permissions import IsSuperAdmin
from apps.education.api.v1.serializers.educaton_serializer import EducationSerializer
from apps.education.models import Education


class EducationListAPI(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    @swagger_auto_schema(
        responses={200: EducationSerializer(many=True)},
        tags=["Education"],
        operation_summary="List educations",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EducationDetailAPI(generics.RetrieveAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    @swagger_auto_schema(
        responses={200: EducationSerializer()},
        tags=["Education"],
        operation_summary="Retrieve an education",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EducationCreateAPI(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=EducationSerializer,
        responses={201: EducationSerializer()},
        tags=["Education"],
        operation_summary="Create a new education",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EducationUpdateAPI(generics.UpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=EducationSerializer,
        responses={200: EducationSerializer()},
        tags=["Education"],
        operation_summary="Update an education",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=EducationSerializer,
        responses={200: EducationSerializer()},
        tags=["Education"],
        operation_summary="Partial Update an education",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EducationDeleteAPI(generics.DestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Education"],
        operation_summary="Delete an education",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
