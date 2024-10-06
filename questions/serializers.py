from rest_framework import serializers
from .models import QuestionAnimal


"""Data conversion to JSON"""
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnimal
        fields = ['photo', 'animal_type', 'weight', 'gender', 'is_stray']
