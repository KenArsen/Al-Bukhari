from apps.us.models.about_us_models import About


class AboutRepository:
    @classmethod
    def get_about(cls):
        return About.objects.all()

    @classmethod
    def get_about_id(cls, about_id):
        return About.objects.get(id=about_id)

