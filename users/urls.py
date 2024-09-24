from django.urls import path,include
from .views import some_view,registration_success


urlpatterns = [

    path('social-auth/',
         include('social_django.urls', namespace='social')), #social-auth

    path('index', some_view, name='some_view'),

    path('registration', registration_success, name='registration_success')

]

