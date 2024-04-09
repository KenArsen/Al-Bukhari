import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from urllib.parse import urljoin


class CkeditorCustomStorage(FileSystemStorage):
    location = os.path.join(settings.MEDIA_ROOT, 'uploads/')
    base_url = urljoin(settings.MEDIA_URL, 'uploads/')
