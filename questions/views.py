from rest_framework import generics
from .models import QuestionAnimal
from .serializers import QuestionSerializer

class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = QuestionAnimal.objects.all()
    serializer_class = QuestionSerializer

