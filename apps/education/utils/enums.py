from django.db import models


class NamazType(models.TextChoices):
    FAJR = "FAJR", "FAJR"
    ZUHR = "ZUHR", "ZUHR"
    ASR = "ASR", "ASR"
    MAGHREB = "MAGHREB", "MAGHREB"
    ISHA = "ISHA", "ISHA"
    VITR = "VITR", "VITR"
