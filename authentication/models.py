from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None):
        if username is None:
            username = email.split("@", 1)[0]
        if email is None:
            raise TypeError("Email must not be Empty")
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username=None):
        if password is None:
            raise TypeError("Password must not be Empty")
        user = self.create_user(email, password, username)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    fullname = models.CharField(
        max_length=255, null=True, blank=True, default="username"
    )
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    phonenumber = models.CharField(max_length=10, null=True, blank=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELD = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        token = RefreshToken.for_user(self)
        return {"refresh_token": str(token), "access_token": str(token.access_token)}
