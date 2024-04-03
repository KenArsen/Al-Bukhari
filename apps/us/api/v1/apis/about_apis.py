from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from apps.us.api.v1.serializers import AboutUsSerializer
from apps.us.models import About


class AboutListAPI(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AboutDetailAPI(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class AboutCreateAPI(generics.CreateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AboutUpdateAPI(generics.UpdateAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class AboutDeleteAPI(generics.DestroyAPIView):
    queryset = About.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
