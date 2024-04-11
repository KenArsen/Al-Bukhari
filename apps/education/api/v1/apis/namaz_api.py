from rest_framework import exceptions, generics, permissions

from apps.common import IsSuperAdmin
from apps.education.api.v1.serializers import NamazReadSerializer, NamazWriteSerializer
from apps.education.models import Namaz


class NamazListAPI(generics.ListAPIView):
    serializer_class = NamazReadSerializer

    def get_queryset(self):
        queryset = Namaz.objects.all()
        namaz_type = self.request.data.get("namaz_type", None)
        gender = self.request.data.get("gender", None)

        if namaz_type and gender:
            return queryset.filter(namaz_type=namaz_type, gender=gender)
        elif namaz_type and gender is None:
            return queryset.filter(namaz_type=namaz_type)
        elif gender and namaz_type is None:
            raise exceptions.ValidationError({"error": "namaz_type parameter is required"})
        else:
            return queryset


class NamazCreateAPI(generics.CreateAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazWriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class NamazDetailAPI(generics.RetrieveAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazReadSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class NamazUpdateAPI(generics.UpdateAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazWriteSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class NamazDeleteAPI(generics.DestroyAPIView):
    queryset = Namaz.objects.all()
    serializer_class = NamazReadSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
