from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from apps.education.api.v1.serializers import TaharatSerializer
from apps.education.models import Taharat


class TaharatListAPI(generics.ListAPIView):
    queryset = Taharat.objects.all()
    serializer_class = TaharatSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class TaharatCreateAPI(generics.CreateAPIView):
    queryset = Taharat.objects.all()
    serializer_class = TaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TaharatDetailAPI(generics.RetrieveAPIView):
    queryset = Taharat.objects.all()
    serializer_class = TaharatSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class TaharatUpdateAPI(generics.UpdateAPIView):
    queryset = Taharat.objects.all()
    serializer_class = TaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class TaharatDeleteAPI(generics.DestroyAPIView):
    queryset = Taharat.objects.all()
    serializer_class = TaharatSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
