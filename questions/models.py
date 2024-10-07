from django.db import models


"""Question model"""

class Question(models.Model):
    question = models.TextField()
    pet_art = models.CharField(max_length=100)
    pet_weight = models.CharField(max_length=100)
    pet_gender = models.CharField(max_length=50)
    is_homeless = models.BooleanField()
    files = models.FileField(upload_to='questions_files/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question


