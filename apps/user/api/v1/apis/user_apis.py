from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.common.permissions import IsSuperAdmin
from apps.user.api.v1.serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserListSerializer,
    UserProfileSerializer,
    UserUpdateSerializer,
)
from apps.user.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsSuperAdmin]
    detail_serializer_class = UserDetailSerializer
    search_fields = ("first_name", "last_name", "email")
    ordering = ["-updated_at"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        elif self.action == "retrieve":
            return UserDetailSerializer
        elif self.action == "create":
            return UserCreateSerializer
        elif self.action in ["update", "partial_update"]:
            return UserUpdateSerializer
        elif self.action == "profile":
            return UserProfileSerializer

    @action(["get"], detail=False)
    def profile(self, request, *args, **kwargs):
        user = get_object_or_404(User, id=request.user.id)
        serializer = self.get_serializer(user, context={"request": request})
        return Response(serializer.data)
