from rest_framework import generics, permissions

from apps.common.permissions import IsSuperAdmin
from apps.education.api.v1.serializers import EducationCategorySerializer
from apps.education.models import EducationCategory


class EducationCategoryListAPI(generics.ListAPIView):
    queryset = EducationCategory.objects.all()
    serializer_class = EducationCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EducationCategoryDetailAPI(generics.RetrieveAPIView):
    queryset = EducationCategory.objects.all()
    serializer_class = EducationCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EducationCategoryCreateAPI(generics.CreateAPIView):
    queryset = EducationCategory.objects.all()
    serializer_class = EducationCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EducationCategoryUpdateAPI(generics.UpdateAPIView):
    queryset = EducationCategory.objects.all()
    serializer_class = EducationCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class EducationCategoryDeleteAPI(generics.DestroyAPIView):
    queryset = EducationCategory.objects.all()
    serializer_class = EducationCategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
