from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db import models
from django.utils.translation import ugettext


class BaseModel(models.Model):
    # all models should be inheritted from this model
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, BaseModel):
    username = models.CharField(
        ugettext('Username'), max_length=255,
        db_index=True, unique=True
    )
    USERNAME_FIELD = 'username'

    class Meta:
        app_label = 'users'
                     