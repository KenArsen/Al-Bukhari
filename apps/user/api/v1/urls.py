from django.urls import path

from apps.user.api.v1.apis import (
    SendPasswordResetEmailAPI,
    UserChangePasswordAPI,
    UserDeleteAPI,
    UserDetailAPI,
    UserListAPI,
    UserLoginAPI,
    UserPasswordResetAPI,
    UserProfileView,
    UserRegistrationAPI,
    UserUpdateAPI,
)

app_name = "users"

urlpatterns = [
    path("", UserListAPI.as_view(), name="user-list"),
    path("<int:pk>/", UserDetailAPI.as_view(), name="user-detail"),
    path("<int:pk>/update/", UserUpdateAPI.as_view(), name="user-update"),
    path("<int:pk>/delete/", UserDeleteAPI.as_view(), name="user-delete"),
    path("login/", UserLoginAPI.as_view(), name="user-login"),
    path("register/", UserRegistrationAPI.as_view(), name="user-register"),
    path("profile/", UserProfileView.as_view(), name="user-profile"),
    path("change-password/", UserChangePasswordAPI.as_view(), name="user-change-password"),
    path("send-reset-password-email/", SendPasswordResetEmailAPI.as_view(), name="user-send-reset-password-email"),
    path("reset-password/<uid>/<token>/", UserPasswordResetAPI.as_view(), name="user-reset-password"),
]
