from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions

from apps.common import IsSuperAdmin
from .serializers import MenuSerializer
from .models import Menu


class MenuListAPI(generics.ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @swagger_auto_schema(
        responses={200: MenuSerializer(many=True)},
        tags=["Menu"],
        operation_summary="List Menu",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class MenuCreateAPI(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        tags=["Menu"],
        operation_summary="Create Menu",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MenuDetailAPI(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @swagger_auto_schema(
        responses={200: MenuSerializer()},
        tags=["Menu"],
        operation_summary="Retrieve Menu",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class MenuUpdateAPI(generics.UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        request_body=MenuSerializer,
        responses={200: MenuSerializer()},
        tags=["Menu"],
        operation_summary="Update Menu",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        request_body=MenuSerializer,
        responses={200: MenuSerializer()},
        tags=["Menu"],
        operation_summary="Partial Update Menu",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class MenuDeleteAPI(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Menu"],
        operation_summary="Delete Menu",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
