from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.urls import path
from django.http import HttpResponseRedirect


"""Redirect after registration and authorization"""
def custom_login_redirect(request):
    # Получаем URL из сессии или задаем значение по умолчанию
    redirect_url = request.session.get('redirect_url', '/default-url')
    return redirect(redirect_url)


"""Redirect for creating an API for authorization"""

def google_oauth_redirect(request):
    redirect_url = f"{settings.BASE_URL}/users/social-auth/login/google-oauth2/"
    return HttpResponseRedirect(redirect_url)

def facebook_oauth_redirect(request):
    # Используем переменную из settings.py
    redirect_url = f"{settings.BASE_URL}/users/social-auth/login/facebook/"
    return HttpResponseRedirect(redirect_url)






"""Created for testing; it will be removed later"""
def some_view(request):
    return render(request, 'index.html')

def registration_success(request):
    return render(request, 'registration_success.html')

def question_post(request):
    return render(request, 'question.html')
