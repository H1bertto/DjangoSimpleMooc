from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.db import models
import re


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True,
        validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'O nome de Usuário só pode conter letras, números ou os seguintes caracteres _ . - + @',
                'invalid'
            )
        ]
    )
    email = models.EmailField('E-Mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está Ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
