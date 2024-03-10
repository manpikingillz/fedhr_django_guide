import uuid

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager as BUM,
    PermissionsMixin,
    AbstractBaseUser,
    AbstractUser
)

from fedhr.common.models import BaseModel


# Taken from here:
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#a-full-example
# With some modifications


class BaseUserManager(BUM):
    def create_user(self, username, email,
                    is_superuser, is_active=True, is_admin=False,
                    password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email.lower()),
            is_superuser=is_superuser,
            is_active=is_active,
            is_admin=is_admin,
            **extra_fields
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username=username,
            email=email,
            is_active=True,
            is_admin=True,
            is_superuser=True,
            password=password
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user


class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    username = models.CharField(
        verbose_name='Username',
        max_length=150,
        unique=True, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # This should potentially be an encrypted field
    jwt_key = models.UUIDField(default=uuid.uuid4)

    objects = BaseUserManager()

    USERNAME_FIELD = 'username'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
