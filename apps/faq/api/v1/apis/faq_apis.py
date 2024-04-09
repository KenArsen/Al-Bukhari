from rest_framework import generics

from apps.faq.api.v1.serializers import FaqSerializer
from apps.faq.models import Faq


class FaqListAPI(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqDetailAPI(generics.RetrieveAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqCreateAPI(generics.CreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqUpdateAPI(generics.UpdateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer


class FaqDeleteAPI(generics.DestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
