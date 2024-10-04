from django.urls import path
from .views import QuestionCreateAPIView

urlpatterns = [

    path('api/questions/', QuestionCreateAPIView.as_view(), name='question-create'),

]
