from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from apps.education.api.v1.serializers import GhuslSerializer
from apps.education.models import Ghusl


class GhuslListAPI(generics.ListAPIView):
    queryset = Ghusl.objects.all()
    serializer_class = GhuslSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class GhuslCreateAPI(generics.CreateAPIView):
    queryset = Ghusl.objects.all()
    serializer_class = GhuslSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GhuslDetailAPI(generics.RetrieveAPIView):
    queryset = Ghusl.objects.all()
    serializer_class = GhuslSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class GhuslUpdateAPI(generics.UpdateAPIView):
    queryset = Ghusl.objects.all()
    serializer_class = GhuslSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class GhuslDeleteAPI(generics.DestroyAPIView):
    queryset = Ghusl.objects.all()
    serializer_class = GhuslSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
