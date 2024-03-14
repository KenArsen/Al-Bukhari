from django.contrib.auth import authenticate
from rest_framework import serializers


def get_and_authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid email/password. Please try again!")
    return user
