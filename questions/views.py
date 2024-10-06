from rest_framework import generics
from .models import QuestionAnimal
from .serializers import QuestionSerializer


"""View for saving a question to the database"""
class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = QuestionAnimal.objects.all()
    serializer_class = QuestionSerializer


