from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
NONE = None
EXCEEDS = 3
MEETS = 2
EMERGING = 1
DOESNOT = 0
    
QUESTION_CHOICES = (
    (NONE, "----------"),
    (EXCEEDS, 'Exceeds Expectations'),
    (MEETS, 'Meets Expectations'),
    (EMERGING, 'Emerging'),
    (DOESNOT, 'Does Not Meet Expectations'),
)

class firstEvaluation(models.Model):

    fname = models.CharField(max_length = 200, default = "Enter First Name")
    lname = models.CharField(max_length = 200, default = "Enter Last Name")
    stud_id = models.IntegerField(default = 0)
    question1a = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question1b = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question1c = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question1d = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question2e = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question2f = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question2g = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question2h = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question2i = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question3j = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question3k = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question3l = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question4m = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question5a = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question5b = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question5c = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question5d = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question5e = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question6f = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question6g = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question7h = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    comment = models.CharField(max_length = 1000, default = "")
    user = models.ForeignKey(
        User, related_name="firstEvaluation",
        on_delete=models.DO_NOTHING,
        default=1,
    )

    def __str__(self):
        return self.fname + ' - ' + self.lname

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supervise = models.ManyToManyField("self", related_name="supervised_by", symmetrical=False, blank=True)
    student_ID = models.IntegerField(default=0)
    date_modified = models.DateTimeField(User, auto_now=True)

    def __str__(self):
        return self.user.username

#Create Profile when New User Signs Up

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        #Have the user supervise themselves
        user_profile.supervise.set([instance.profile.id])
        user_profile.save()

post_save.connect(create_profile, sender=User)

