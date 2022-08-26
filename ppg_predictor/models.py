from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class League(models.Model):
    leaguename = models.CharField(max_length=25)
    
    

    def __str__(self):
        return self.leaguename


class Team(models.Model):
    teamname = models.CharField(max_length = 25)
    league = models.ForeignKey(League, default = 0, on_delete=models.SET_DEFAULT)
    user = models.ForeignKey(User, default=2,on_delete=models.CASCADE)  #2 is CPU_AI
    
    

    def __str__(self):
        return self.teamname


class Season(models.Model):
    year = models.CharField(max_length=4)
    league=models.ForeignKey(League, default = 0, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return self.year




class Player(models.Model):
    name = models.CharField(max_length = 40)
    age = models.CharField(max_length = 2)
    mpg = models.FloatField()
    years = models.CharField(max_length = 2)
    draftPos = models.CharField(max_length = 2)
    salary = models.CharField(max_length = 9)
    ppg2022 = models.FloatField()
    predictedppg = models.FloatField()
    potential = models.FloatField()
    team = models.ForeignKey(Team, default=0, on_delete=models.SET_DEFAULT)
    

    def __str__(self):
        return self.name
