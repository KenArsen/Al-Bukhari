from apps.education.repositories import EducationRepository


class EducationService:
    def __init__(self, repository: EducationRepository):
        self._repository = repository
