from rest_framework import status

from apps.event.repositories import EventRepository
from apps.event.serializers import EventSerializer
from apps.image.models import Image
from apps.image.serializers import ImageSerializer


class EventListService:
    @classmethod
    def get_events(cls):
        events = EventRepository.get_events()
        serializer = EventSerializer(events, many=True)
        return serializer.data


class EventRetrieveService:
    @classmethod
    def get_event(cls, pk):
        event = EventRepository.get_event_by_id(event_id=pk)
        serializer = EventSerializer(event)
        return serializer.data


class EventCreateService:
    @classmethod
    def create_event(cls, event):
        event_data = event.data
        event_serializer = EventSerializer(data=event_data)
        if event_serializer.is_valid():
            event_instance = event_serializer.save()
<<<<<<< HEAD
            images = event.FILES.getlist('images')
            for image in images:
                image_serializer = ImageSerializer(data={'image': image})
=======
            images = event.FILES.getlist("images")
            for image in images:
                image_serializer = ImageSerializer(data={"image": image})
>>>>>>> 24677ec (added STATICFILES_DIRS)
                if image_serializer.is_valid():
                    image_instance = image_serializer.save()
                    event_instance.images.add(image_instance)
                else:
                    return image_serializer.errors, status.HTTP_400_BAD_REQUEST

            return event_serializer.data, status.HTTP_201_CREATED
        else:
            return event_serializer.errors, status.HTTP_400_BAD_REQUEST


class EventUpdateService:
    @classmethod
    def update_event(cls, pk, event_data):
        instance = EventRepository.get_event_by_id(event_id=pk)
        event_serializer = EventSerializer(instance, data=event_data)
        if event_serializer.is_valid():
            event_instance = event_serializer.save()

<<<<<<< HEAD
            images_data = event_data.getlist('images', [])
            for image_data in images_data:
                # Если передается id изображения, оно может быть удалено из связи
                image_id = image_data.get('id')
=======
            images_data = event_data.getlist("images", [])
            for image_data in images_data:
                # Если передается id изображения, оно может быть удалено из связи
                image_id = image_data.get("id")
>>>>>>> 24677ec (added STATICFILES_DIRS)
                if image_id:
                    try:
                        image_instance = Image.objects.get(id=image_id)
                        event_instance.images.remove(image_instance)
                    except Image.DoesNotExist:
                        pass

                # Создание или обновление изображений
                image_serializer = ImageSerializer(data=image_data)
                if image_serializer.is_valid():
                    image_instance = image_serializer.save()
                    event_instance.images.add(image_instance)
                else:
                    return image_serializer.errors, status.HTTP_400_BAD_REQUEST

            return event_serializer.data, None
        else:
            return event_serializer.errors, status.HTTP_400_BAD_REQUEST


class EventDeleteService:
    @classmethod
    def delete_event(cls, pk):
        event = EventRepository.get_event_by_id(event_id=pk)
        if event:
            # Удаляем связанные изображения
            event.images.clear()
            # Удаляем само событие
            event.delete()
            return status.HTTP_204_NO_CONTENT
        return status.HTTP_404_NOT_FOUND
