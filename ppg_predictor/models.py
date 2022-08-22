from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length = 40)
    age = models.CharField(max_length = 2)
    mpg = models.FloatField()
    years = models.CharField(max_length = 2)
    draftPos = models.CharField(max_length = 2)
    salary = models.CharField(max_length = 9)
    ppg2022 = models.FloatField()
    predictedppg = models.FloatField()

    def __str__(self):
        return self.name