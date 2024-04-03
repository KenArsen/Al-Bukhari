from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from apps.service.api.v1.serializers import (
    ServiceReadSerializer,
    ServiceWriteSerializer,
)
from apps.service.models import Service


class ServiceListAPI(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceReadSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ServiceDetailAPI(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceReadSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ServiceCreateAPI(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceWriteSerializer
    # permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ServiceUpdateAPI(generics.UpdateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceWriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ServiceDeleteAPI(generics.DestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceReadSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
