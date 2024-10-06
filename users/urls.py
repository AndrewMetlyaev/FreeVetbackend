from django.urls import path,include
from .views import (some_view,registration_success, custom_login_redirect,question_post,google_oauth_redirect,
facebook_oauth_redirect)


urlpatterns = [

    path('social-auth/',
         include('social_django.urls', namespace='social')), #social-auth

    path('redirect/', custom_login_redirect, name='custom_login_redirect'), #Redirect after registration and authorization

    path('login/google/', google_oauth_redirect, name='google-login-shortcut'), #Short API for authorization google

    path('login/facebook/', facebook_oauth_redirect, name='facebook-login-shortcut'), #Short API for authorization facebook



#The paths below are created for testing; they will be removed later

    path('index', some_view, name='some_view'),

    path('registration', registration_success, name='registration_success'),

    path('question_post', question_post, name='question_post')

]

