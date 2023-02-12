from django.db import models

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

    def __str__(self):
        return self.fname + ' - ' + self.lname