from apps.us.api.v1.repositories.about_repository import AboutRepository
from apps.us.api.v1.serializers.about_serializer import AboutUsSerializer

from rest_framework import status


class AboutListService:
    @classmethod
    def get_about(cls):
        about = AboutRepository.get_about()
        serializer = AboutUsSerializer(about, many=True)
        return serializer.data


class AboutRetrieveService:
    @classmethod
    def get_about(cls, pk):
        about = AboutRepository.get_about_id(about_id=pk)
        serializer = AboutUsSerializer(about)
        return serializer.data


class AboutCreateService:
    @classmethod
    def create_about(cls, data):
        about_serializer = AboutUsSerializer(data=data)
        if about_serializer.is_valid():
            about_serializer.save()
            return about_serializer.data


class AboutUpdateService:
    @classmethod
    def update_about(cls, pk, about_data):
        instance = AboutRepository.get_about_id(about_id=pk)
        about_serializer = AboutUsSerializer(instance, data=about_data)
        if about_serializer.is_valid():
            about_serializer.save()
            return about_serializer.data


class AboutDeleteService:
    @classmethod
    def delete_about(cls, pk):
        about = AboutRepository.get_about_id(about_id=pk)
        if about:
            about.delete()
            return status.HTTP_204_NO_CONTENT

        return status.HTTP_404_NOT_FOUND


