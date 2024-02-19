from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Permission, который разрешает доступ только администраторам.
    """

    def has_permission(self, request, view):
        """
        Проверка, является ли пользователь администратором.
        """
        return request.user and request.user.is_superuser
