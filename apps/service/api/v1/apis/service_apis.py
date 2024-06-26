from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from apps.common import IsSuperAdmin
from apps.service.api.v1.serializers import (
    ServiceReadSerializer,
    ServiceSendSerializer,
    ServiceWriteSerializer,
)
from apps.service.models import Service
from apps.service.tasks import send


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
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

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


class SendEmailAPI(views.APIView):
    from drf_yasg import openapi
    from drf_yasg.utils import swagger_auto_schema

    @swagger_auto_schema(
        operation_summary="Sending email",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "service": openapi.Schema(type=openapi.TYPE_STRING, description="Choice one service"),
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Name of the sender"),
                "email": openapi.Schema(
                    type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description="Email of the sender"
                ),
                "message": openapi.Schema(type=openapi.TYPE_STRING, description="Message content"),
            },
            required=["name", "email", "message"],
        ),
    )
    def post(self, request, *args, **kwargs):
        serializer = ServiceSendSerializer(data=request.data)
        if serializer.is_valid():
            send.delay(**serializer.validated_data)
            return Response({"success": "OK"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
