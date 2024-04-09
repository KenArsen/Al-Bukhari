from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.common import permissions
from apps.update.api.v1.serializers import UpdateSerializer
from apps.update.models import Update


class UpdateListAPI(generics.ListAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer


class UpdateDetailAPI(generics.RetrieveAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer


class CreateUpdateAPI(generics.CreateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticated, permissions.IsSuperAdmin]


class UpdateUpdateAPI(generics.UpdateAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticated, permissions.IsSuperAdmin]


class DeleteUpdateAPI(generics.DestroyAPIView):
    queryset = Update.objects.all()
    serializer_class = UpdateSerializer
    permission_classes = [IsAuthenticated, permissions.IsSuperAdmin]
