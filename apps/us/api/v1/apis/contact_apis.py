from rest_framework import generics, permissions, status, views, viewsets
from rest_framework.response import Response

from apps.common import IsSuperAdmin
from apps.us.api.v1.serializers import (
    ContactSendSerializer,
    ContactSerializer,
    UrlSerializer,
)
from apps.us.models import Contact, Url
from apps.us.tasks import send


class UrlVewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]


class ContactListAPI(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ContactCreateAPI(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContactDetailAPI(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ContactUpdateAPI(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ContactDeleteAPI(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
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
        serializer = ContactSendSerializer(data=request.data)
        if serializer.is_valid():
            send.delay(**serializer.validated_data)
            return Response({"success": "OK"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
