from django.db import models
from data.models import *

# Create your models here.

class Game(models.Model):
    # repository that the file is uploaded to
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    # previous question
    previous_question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, blank=True)

    total_score = models.IntegerField()
    
    questions_done = models.IntegerField()