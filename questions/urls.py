from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import add_question

urlpatterns = [
    path('api/add/', add_question, name='add_question'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
