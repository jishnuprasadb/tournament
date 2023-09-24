from django.db import models

# Create your models here.
class Team(models.Model):
    name=models.CharField(max_length=255)
    manager=models.CharField(max_length=255)
    coach=models.CharField(max_length=255)
    contact=models.CharField(max_length=255)

class Players(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)    
    name=models.CharField(max_length=255)

class Score(models.Model):
    match_no=models.IntegerField()
    score=models.CharField(max_length=255)