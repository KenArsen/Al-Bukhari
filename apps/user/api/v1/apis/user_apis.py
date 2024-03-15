from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common import IsSuperAdmin
from apps.user.api.v1.serializers import (
    SendPasswordResetEmailSerializer,
    UserChangePasswordSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserLoginSerializer,
    UserPasswordResetSerializer,
    UserProfileSerializer,
    UserRegistrationSerializer,
    UserUpdateSerializer,
)
from apps.user.models import User


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    @swagger_auto_schema(
        tags=["Users"], operation_summary="Retrieve a list of users", responses={200: "Returns a list of users"}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Retrieve user details",
        responses={200: "Returns details of the requested user"},
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserUpdateAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Update user information",
        request_body=UserUpdateSerializer,
        responses={200: "Returns updated user data"},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Update user information",
        request_body=UserUpdateSerializer,
        responses={200: "Returns updated user data"},
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserDeleteAPI(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = None

    @swagger_auto_schema(tags=["Users"], operation_summary="Delete user", responses={204: "No content"})
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserLoginAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = UserLoginSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="User login",
        operation_description="Endpoint for user authentication and login.",
        request_body=UserLoginSerializer,
        responses={
            200: "Returns token and success message on successful login",
            404: "Returns error message if email or password is not valid",
        },
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get("email")
        password = serializer.data.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({"token": token, "msg": "Login Success"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"errors": {"non_field_errors": ["Email or Password is not Valid"]}}, status=status.HTTP_404_NOT_FOUND
            )


class UserRegistrationAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="User registration",
        request_body=UserRegistrationSerializer,
        responses={201: "Returns token and success message on successful registration"},
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({"token": token, "msg": "Registration Success"}, status=status.HTTP_201_CREATED)


class UserProfileView(generics.GenericAPIView):
    queryset = None
    serializer_class = UserProfileSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="User profile",
        operation_description="Endpoint to retrieve user profile details.",
        responses={200: "Returns user profile data"},
    )
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = UserChangePasswordSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Change user password",
        request_body=UserChangePasswordSerializer,
        responses={200: "Returns success message upon successful password change"},
    )
    def post(self, request):
        serializer = UserChangePasswordSerializer(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Changed Successfully"}, status=status.HTTP_200_OK)


class SendPasswordResetEmailAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = SendPasswordResetEmailSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Send password reset email",
        operation_description="Endpoint to send an email with a password reset link.",
        request_body=SendPasswordResetEmailSerializer,
        responses={200: "Returns success message upon successful email sending"},
    )
    def post(self, request):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Reset link send. Please check your Email"}, status=status.HTTP_200_OK)


class UserPasswordResetAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = UserPasswordResetSerializer

    @swagger_auto_schema(
        tags=["Users"],
        operation_summary="Reset user password",
        operation_description="Endpoint to reset user password using a token received via email.",
        request_body=UserPasswordResetSerializer,
        responses={200: "Returns success message upon successful password reset"},
    )
    def post(self, request, uid, token):
        serializer = UserPasswordResetSerializer(data=request.data, context={"uid": uid, "token": token})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Reset Successfully"}, status=status.HTTP_200_OK)
