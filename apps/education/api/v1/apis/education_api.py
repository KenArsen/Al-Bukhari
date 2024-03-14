from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, permissions, status, views
from rest_framework.response import Response

from apps.common.permissions import IsAdmin
from apps.education.api.v1.serializers.educaton_serializer import EducationSerializer
from apps.education.repositories import EducationRepository


class EducationListAPI(views.APIView):
    @swagger_auto_schema(
        responses={200: EducationSerializer(many=True)},
        tags=["Education"],
        operation_summary="List educations",
    )
    def get(self, request):
        educations = EducationRepository().get_educations()
        serializer = EducationSerializer(educations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EducationDetailAPI(views.APIView):
    @swagger_auto_schema(
        responses={200: EducationSerializer()},
        tags=["Education"],
        operation_summary="Retrieve an education",
    )
    def get(self, request, pk):
        education = EducationRepository().get_education_by_id(education_id=pk)
        serializer = EducationSerializer(education)
        return Response(serializer.data, status=status.HTTP_200_OK)


class EducationCreateAPI(views.APIView):
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        request_body=EducationSerializer,
        responses={201: EducationSerializer()},
        tags=["Education"],
        operation_summary="Create a new education",
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationUpdateAPI(views.APIView):
    queryset = EducationRepository().get_educations()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        request_body=EducationSerializer,
        responses={200: EducationSerializer()},
        tags=["Education"],
        operation_summary="Update an education",
    )
    def put(self, request, pk):
        education = generics.get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        request_body=EducationSerializer,
        responses={200: EducationSerializer()},
        tags=["Education"],
        operation_summary="Partial Update an education",
    )
    def patch(self, request, pk):
        education = generics.get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(education, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EducationDeleteAPI(views.APIView):
    queryset = EducationRepository().get_educations()
    serializer_class = EducationSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    @swagger_auto_schema(
        responses={204: "No content"},
        tags=["Education"],
        operation_summary="Delete an education",
    )
    def delete(self, request, pk):
        education = generics.get_object_or_404(self.queryset, pk=pk)
        education.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
