from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_provider = models.CharField(max_length=50, blank=True, null=True)  # Социальная сеть
    first_name = models.CharField(max_length=30, blank=True, null=True)     # Имя
    last_name = models.CharField(max_length=30, blank=True, null=True)      # Фамилия
    email = models.EmailField(unique=True, blank=True, null=True)           # Почта
    registration_time = models.DateTimeField(auto_now_add=True)             # Время регистрации
    last_login_time = models.DateTimeField(auto_now=True)                   # Время последнего входа

    def __str__(self):
        return self.user.username
