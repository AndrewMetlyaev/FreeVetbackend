from django.db import models


"""Question model"""
class QuestionAnimal(models.Model):
    photo = models.ImageField(upload_to='questions/photos/', blank=True, null=True)
    animal_type = models.CharField(max_length=50)
    weight = models.FloatField()
    gender = models.CharField(max_length=10)
    is_stray = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.animal_type} ({self.weight} kg)"
