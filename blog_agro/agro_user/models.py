from django.contrib.auth.models import UserManager, AbstractUser
from django.db import models


class AgroUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    username = models.CharField('username', max_length=100, unique=True)
    first_name = models.CharField('first_name', max_length=100, null=True, blank=True)
    last_name = models.CharField('last_name', max_length=100, null=True, blank=True)
    email = models.EmailField('email', max_length=100, null=True, unique=True)
    is_client = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']