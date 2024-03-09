from apps.event.models import Event


class EventRepository:
    @classmethod
    def get_all(cls):
        return Event.objects.prefetch_related("images").all()

    @classmethod
    def get_by_id(cls, pk):
        return Event.objects.prefetch_related("images").get(pk=pk)
