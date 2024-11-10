from .models import Question, QuestionFile
from rest_framework import serializers

class QuestionFileSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()  # Поле для полного URL файла

    class Meta:
        model = QuestionFile
        fields = ['file_url']  # Включаем только поле с URL файла

    def get_file_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.file.url) if request else obj.file.url


class QuestionSerializer(serializers.ModelSerializer):
    files = QuestionFileSerializer(many=True, read_only=True)  # Используем related_name 'files'

    class Meta:
        model = Question
        exclude = ['user_id']  # Исключаем поле user_id
