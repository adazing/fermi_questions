from django.db import models

# Create your models here.

# repository
class Repository(models.Model):
    # name of the repository
    name=models.CharField(max_length=500)

# file with all the questions
class File(models.Model):
    # repository that the file is uploaded to
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    # name of the file
    name=models.CharField(max_length=500)

class Question(models.Model):
    # file that the question came from
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    # query (question text)
    query = models.TextField()
    # answer (int)
    answer = models.IntegerField()
    # number of times the question is done
    experience = models.IntegerField()
    # number of times the skill is done
    skill = models.IntegerField()


# future ideas:
    # modes: combo (practice with another person) vs solo (practice alone)