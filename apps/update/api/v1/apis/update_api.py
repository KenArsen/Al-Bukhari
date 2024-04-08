from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.common import permissions
from apps.update.api.v1.serializers import UpdateModelSerializer
from apps.update.models import UpdateModel


class UpdateListAPI(generics.ListAPIView):
    queryset = UpdateModel.objects.all()
    serializer_class = UpdateModelSerializer


class UpdateDetailAPI(generics.RetrieveAPIView):
    queryset = UpdateModel.objects.all()
    serializer_class = UpdateModelSerializer


class CreateUpdateAPI(generics.CreateAPIView):
    queryset = UpdateModel.objects.all()
    serializer_class = UpdateModelSerializer
    permission_classes = [IsAuthenticated, permissions.IsSuperAdmin]


class UpdateUpdateAPI(generics.UpdateAPIView):
    queryset = UpdateModel.objects.all()
    serializer_class = UpdateModelSerializer
    permission_classes = [IsAuthenticated, permissions.IsSuperAdmin]


class DeleteUpdateAPI(generics.DestroyAPIView):
    queryset = UpdateModel.objects.all()
    serializer_class = UpdateModelSerializer
    permission_classes = [IsAuthenticated, permissions.IsSuperAdmin]
