from django.urls import path

from apps.user.api.v1.apis import (
    SendPasswordResetEmailAPI,
    UserChangePasswordAPI,
    UserLoginAPI,
    UserPasswordResetAPI,
    UserProfileAPI,
    UserRegistrationAPI,
)

app_name = "users"

urlpatterns = [
    path("register/", UserRegistrationAPI.as_view(), name="user-register"),
    path("login/", UserLoginAPI.as_view(), name="user-login"),
    path("profile/", UserProfileAPI.as_view(), name="user-profile"),
    path("change-password/", UserChangePasswordAPI.as_view(), name="user-change-password"),
    path("send-reset-password-email/", SendPasswordResetEmailAPI.as_view(), name="user-send-reset-password-email"),
    path("reset-password/<uid>/<token>/", UserPasswordResetAPI.as_view(), name="user-reset-password"),
]
