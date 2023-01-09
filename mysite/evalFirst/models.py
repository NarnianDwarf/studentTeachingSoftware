from django.db import models

# Create your models here.

class firstEvaluation(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    student_id = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

# class firstQuestions(models.Model):
#     firstEvaluation = models.ForeignKey(firstEvaluation, on_delete=models.CASCADE)
#     question1 = forms.ModelChoiceField(queryset=['Below', 'Average', 'Above'])

#     def __str__(self):
#         return self.question1