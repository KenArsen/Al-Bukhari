from rest_framework import generics, permissions

from apps.common.permissions import IsSuperAdmin
from apps.education.api.v1.serializers.educaton_serializer import (
    EducationDetailSerializer,
    EducationSerializer,
    EducationWriteSerializer,
)
from apps.education.models import Education


class EducationListAPI(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EducationDetailAPI(generics.RetrieveAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EducationCreateAPI(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationWriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EducationUpdateAPI(generics.UpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationWriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EducationDeleteAPI(generics.DestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
