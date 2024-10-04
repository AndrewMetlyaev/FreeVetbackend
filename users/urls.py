from django.urls import path,include
from .views import some_view,registration_success, custom_login_redirect,question_post


urlpatterns = [

    path('social-auth/',
         include('social_django.urls', namespace='social')), #social-auth

    path('redirect/', custom_login_redirect, name='custom_login_redirect'),

    path('index', some_view, name='some_view'),

    path('registration', registration_success, name='registration_success'),

    path('question_post', question_post, name='question_post')

]

