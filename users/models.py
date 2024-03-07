from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True)
    citi = models.CharField(max_length=100, verbose_name='Город', blank=True)
    photo = models.ImageField(upload_to='users', verbose_name='Аватар', blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
