from django.urls import path

from apps.user.api.v1.apis import (
    SendPasswordResetEmailAPI,
    UserChangePasswordAPI,
    UserLoginAPI,
    UserPasswordResetAPI,
    UserRegistrationAPI,
    UserViewSet,

)
from rest_framework.routers import DefaultRouter

app_name = "users"

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path("login/", UserLoginAPI.as_view(), name="user-login"),
    path("register/", UserRegistrationAPI.as_view(), name="user-register"),
    path("change-password/", UserChangePasswordAPI.as_view(), name="user-change-password"),
    path("send-reset-password-email/", SendPasswordResetEmailAPI.as_view(), name="user-send-reset-password-email"),
    path("reset-password/<uid>/<token>/", UserPasswordResetAPI.as_view(), name="user-reset-password"),
]

urlpatterns += router.urls
