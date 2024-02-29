from apps.education.models import Education


class EducationRepository:
    @classmethod
    def get_educations(cls):
        return Education.objects.all()

    @classmethod
    def get_education_by_id(cls, education_id):
        return Education.objects.get(pk=education_id)
