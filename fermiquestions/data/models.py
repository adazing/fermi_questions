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
    file = models.ForeignKey(File, on_delete=models.CASCADE, null=True, blank=True)
    #repository that the question came from
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    # query (question text)
    query = models.TextField()
    # answer (int)
    answer = models.IntegerField()
    # number of times the question is attempted
    experience = models.IntegerField(default = 0)
    # number right vs number wrong (positive = more right, negative = more wrong)
    skill = models.IntegerField(default = 0)
    
    date_made = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['experience', 'skill', '-date_made']

# future ideas:
    # modes: combo (practice with another person) vs solo (practice alone)
    # send all form data to frontend? idk but then cant do improvements bc dont send data back to backend...
    
# robot ideas
    # main problems last competition? what abt good stuff?
    # better imu?
    # pausing robot?
    # smaller robot? - 2 levels?
    # wheels -- are good?
    # how to get accurate time
    # caster wheel change?
    # motor change?
    # use distance sensor? multiple distance sensors?
    # weight to have more friction for robot?
    # delay penalties?
    # rules?

# notes during talk
'''
    better imu - yes
    pausing robot - yes, but prob not necessary to get pretty good time
    smaller robot - yes
    wheels - worry later
    caster wheel - its good
    try 4 motors - maybe only need one motor controller? idk look at how motors need to move when going forward or turning
    distance sensor - too many pins? voltage? do 4 motors first
    weight - sketchy
    delay penalties - prob not
    ensure less than 3 sec waiting time.
    arduino mega - sure if we need, but would be expensive
'''

# forensics notes
    # glucose, sucrose, coffee, nicotene?
    # hair
    # acronyms