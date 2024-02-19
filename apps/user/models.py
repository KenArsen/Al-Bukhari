from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from apps.common.base import BaseModel
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin,):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
