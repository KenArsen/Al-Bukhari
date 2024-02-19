from apps.event.models import Event


class EventRepository:
    @classmethod
    def get_events(cls):
<<<<<<< HEAD
        return Event.objects.prefetch_related('images').all()

    @classmethod
    def get_event_by_id(cls, event_id):
        return Event.objects.prefetch_related('images').get(id=event_id)
=======
        return Event.objects.prefetch_related("images").all()

    @classmethod
    def get_event_by_id(cls, event_id):
        return Event.objects.prefetch_related("images").get(id=event_id)
>>>>>>> 24677ec (added STATICFILES_DIRS)
