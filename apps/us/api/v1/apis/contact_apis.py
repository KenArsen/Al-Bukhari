from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, viewsets

from apps.us.api.v1.serializers import ContactSerializer, UrlSerializer
from apps.us.models import Contact, Url


class UrlVewSet(viewsets.ModelViewSet):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer


class ContactListAPI(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        responses={200: ContactSerializer(many=True)},
        tags=["Contact"],
        operation_summary="List all contacts",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ContactCreateAPI(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        responses={201: ContactSerializer()},
        tags=["Contact"],
        operation_summary="Create a new contact",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ContactDetailAPI(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        responses={200: ContactSerializer()},
        tags=["Contact"],
        operation_summary="Retrieve contact details",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ContactUpdateAPI(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        responses={200: ContactSerializer()},
        tags=["Contact"],
        operation_summary="Update existing contact",
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        responses={200: ContactSerializer()},
        tags=["Contact"],
        operation_summary="Partially update existing contact",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ContactDeleteAPI(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Contact"],
        operation_summary="Delete existing contact",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
