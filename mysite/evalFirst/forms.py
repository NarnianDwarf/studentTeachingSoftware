from django import forms

class firstEvaluationForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length = 200)
    last_name = forms.CharField(label="Last Name", max_length = 200)
    student_id = forms.IntegerField(required = True, label="Student ID")

class firstQuestionsForm(forms.Form):
    EXCEEDS = 3
    MEETS = 2
    EMERGING = 1
    DOESNOT = 0
        
    QUESTION_CHOICES = [
        (None, '----------'),
        (EXCEEDS, 'Exceeds Expectations'),
        (MEETS, 'Meets Expectations'),
        (EMERGING, 'Emerging'),
        (DOESNOT, 'Does Not Meet Expectations'),
    ]

    question1 = forms.ChoiceField(label="Focus for Learning: Standards and Objectives/Targets", choices = QUESTION_CHOICES)
    # Need to add in the rest of the questions and label them properly based off the PDF on teams