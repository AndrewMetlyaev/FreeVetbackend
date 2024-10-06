from django.urls import path
from .views import QuestionCreateAPIView


"""API for creating a question"""
urlpatterns = [

    path('api/questions/', QuestionCreateAPIView.as_view(), name='question-create'),

]
