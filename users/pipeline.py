
"""PIPELINE для создания профиля пользвователя в БД"""

from django.contrib.auth.models import User
from .models import Profile

def save_profile(backend, user, response, *args, **kwargs):
    # Получаем или создаем профиль пользователя
    profile, created = Profile.objects.get_or_create(user=user)

    # Получаем данные из ответа
    if backend.name == 'facebook':
        profile.auth_provider = 'Facebook'
        profile.first_name = response.get('first_name', '')
        profile.last_name = response.get('last_name', '')
        profile.email = response.get('email', '')
    elif backend.name == 'google-oauth2':
        profile.auth_provider = 'Google'
        profile.first_name = response.get('given_name', '')
        profile.last_name = response.get('family_name', '')
        profile.email = response.get('email', '')
    elif backend.name == 'apple':
        profile.auth_provider = 'Apple'
        profile.first_name = response.get('name', {}).get('firstName', '')
        profile.last_name = response.get('name', {}).get('lastName', '')
        profile.email = response.get('email', '')

    # Обновление информации из auth_user
    profile.last_login_time = user.last_login  # Время последнего входа
    profile.registration_time = user.date_joined  # Время регистрации

    # Сохраняем изменения
    profile.save()
