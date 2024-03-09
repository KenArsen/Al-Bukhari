from apps.education.models import Namaz


class NamazRepository:
    @classmethod
    def get_all(cls):
        return Namaz.objects.prefetch_related("images").all()

    @classmethod
    def get_by_id(cls, pk):
        return Namaz.objects.prefetch_related("images").get(pk=pk)
