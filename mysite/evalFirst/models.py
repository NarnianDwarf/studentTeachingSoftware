from django.db import models

# Create your models here.

class firstEvaluation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_id = models.IntegerField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

class firstQuestions(models.Model):
    # firstEvaluation = models.ForeignKey(firstEvaluation, on_delete=models.CASCADE)
    # question1 = forms.ModelChoiceField(queryset=['Below', 'Average', 'Above'])
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_id = models.IntegerField(default=0)

    EXCEEDS = 3
    MEETS = 2
    EMERGING = 1
    DOESNOT = 0
        
    QUESTION_CHOICES = [
        (EXCEEDS, 'Exceeds Expectations'),
        (MEETS, 'Meets Expectations'),
        (EMERGING, 'Emerging'),
        (DOESNOT, 'Does Not Meet Expectations'),
    ]
    
    question1 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question2 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question3 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question4 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question5 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question6 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question7 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question8 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question9 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question10 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question11 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question12 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question13 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question14 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question15 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question16 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question17 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question18 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question19 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question20 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    question21 = models.IntegerField(choices = QUESTION_CHOICES, default = 0)
    
    comment = models.CharField(max_length = 1000)
    def __str__(self):
        return self.question1