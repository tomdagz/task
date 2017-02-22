# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        email = self.normalize_email(email)
        
        if not email:
            raise ValueError('El email debe ser obligatorio')

        user = self.model(email=email, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extrafields):
        return self._create_user(email,password,False,False,**extrafields)

    def create_superuser(self, email, password=None, **extrafields):
        return self._create_user(email,password,True,True,**extrafields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    # REQUIRED_FIELDS = ['email']

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email