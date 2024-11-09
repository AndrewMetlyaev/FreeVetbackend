from .models import Question, QuestionFile
from rest_framework import serializers

class QuestionFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionFile
        fields = ['file']  # Включаем только поле с файлом


class QuestionSerializer(serializers.ModelSerializer):
    files = QuestionFileSerializer(many=True, read_only=True)  # Включаем связанные файлы
    
    class Meta:
        model = Question
        exclude = ['user_id']  # Исключаем поле user_id

