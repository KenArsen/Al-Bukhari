from django.contrib.auth import authenticate
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
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetailAPI(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class UserUpdateAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UserDeleteAPI(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = None
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserLoginAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = UserLoginSerializer

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

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({"token": token, "msg": "Registration Success"}, status=status.HTTP_201_CREATED)


class UserProfileView(generics.GenericAPIView):
    queryset = None
    serializer_class = UserProfileSerializer

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = UserChangePasswordSerializer
    permission_classes = [IsAuthenticated, IsSuperAdmin]

    def post(self, request):
        serializer = UserChangePasswordSerializer(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Changed Successfully"}, status=status.HTTP_200_OK)


class SendPasswordResetEmailAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = SendPasswordResetEmailSerializer

    def post(self, request):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Reset link send. Please check your Email"}, status=status.HTTP_200_OK)


class UserPasswordResetAPI(generics.GenericAPIView):
    queryset = None
    serializer_class = UserPasswordResetSerializer

    def post(self, request, uid, token):
        serializer = UserPasswordResetSerializer(data=request.data, context={"uid": uid, "token": token})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Reset Successfully"}, status=status.HTTP_200_OK)
