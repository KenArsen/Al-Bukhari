from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from apps.education.api.v1.serializers import GhuslAndTaharatSerializer
from apps.education.models import GhuslAndTaharat


class GhuslAndTaharatListAPI(generics.ListAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GhuslAndTaharatCreateAPI(generics.CreateAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GhuslAndTaharatDetailAPI(generics.RetrieveAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GhuslAndTaharatUpdateAPI(generics.UpdateAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class GhuslAndTaharatDeleteAPI(generics.DestroyAPIView):
    queryset = GhuslAndTaharat.objects.all()
    serializer_class = GhuslAndTaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
