<<<<<<< HEAD
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
=======
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
>>>>>>> 24677ec (added STATICFILES_DIRS)
from django.db import models
from apps.common.base import BaseModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
<<<<<<< HEAD

    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Users must have an email address.')
=======
    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError("Users must have an email address.")
>>>>>>> 24677ec (added STATICFILES_DIRS)

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.password = make_password(password)  # Используем make_password для шифрования пароля
        user.save()
        return user

    def create_superuser(self, email, password=None):
        if password is None:
<<<<<<< HEAD
            raise TypeError('Superusers must have a password.')
=======
            raise TypeError("Superusers must have a password.")
>>>>>>> 24677ec (added STATICFILES_DIRS)

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user


<<<<<<< HEAD
class User(BaseModel, AbstractBaseUser, PermissionsMixin, ):
=======
class User(BaseModel, AbstractBaseUser, PermissionsMixin):
>>>>>>> 24677ec (added STATICFILES_DIRS)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

<<<<<<< HEAD
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
=======
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
>>>>>>> 24677ec (added STATICFILES_DIRS)

    objects = UserManager()

    class Meta:
<<<<<<< HEAD
        ordering = ('-id',)
=======
        ordering = ("-id",)
>>>>>>> 24677ec (added STATICFILES_DIRS)
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
