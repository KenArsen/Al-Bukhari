from rest_framework import generics, permissions

from apps.common.permissions import IsSuperAdmin
from apps.education.api.v1.serializers import EducationListSerializer
from apps.education.models import Education


class EducationListListAPI(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EducationListDetailAPI(generics.RetrieveAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationListSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EducationListCreateAPI(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationListSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EducationListUpdateAPI(generics.UpdateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationListSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EducationListDeleteAPI(generics.DestroyAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationListSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
