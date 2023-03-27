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

EVALUATION_NUMBER = (
    (0, "----------"),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
)

class firstEvaluation(models.Model):
    first_Name = models.CharField(db_column = 'First Name', max_length = 200, default = "Enter First Name")
    last_Name = models.CharField(db_column = 'Last Name', max_length = 200, default = "Enter Last Name")
    stud_id = models.IntegerField(db_column = 'Student ID', default = 0)
    # fname = models.CharField(max_length = 200, default = "Enter First Name")
    # lname = models.CharField(max_length = 200, default = "Enter Last Name")
    # stud_id = models.IntegerField(default = 0)
    Evaluation_Number = models.IntegerField(choices = EVALUATION_NUMBER, default = 0)
    date = models.DateField(default = "2023-01-01")
    Pedagogy_A = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_B = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_C = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_D = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_E = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_F = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_G = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_H = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_I = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_J = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_K = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_L = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Pedagogy_M = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_A = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_B = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_C = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_D = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_E = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_F = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_G = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    Disposition_H = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    comment = models.CharField(max_length = 1000, default = "")
    user = models.ForeignKey(
        User, related_name="firstEvaluation",
        on_delete=models.DO_NOTHING,
        default=1,
    )

    # class Meta:
    #     db_table = 'FirstEval'

    def __str__(self):
        return self.first_Name + ' - ' + self.last_Name

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    supervise = models.ManyToManyField("self", related_name="supervised_by", symmetrical=False, blank=True)
    temp_admin = models.IntegerField(default=0) #0 student, #1 admin
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

