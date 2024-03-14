from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.base import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, password2=None, **extra_fields):
        if email is None:
            raise TypeError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.password = make_password(password)  # Используем make_password для шифрования пароля
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, password=None, password2=None):
        if password is None:
            raise TypeError("Superusers must have a password.")

        user = self.create_user(email, first_name, last_name, password, password2)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = UserManager()

    class Meta:
        ordering = ("-id",)
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
