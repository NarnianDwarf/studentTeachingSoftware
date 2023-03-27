from django import forms
from django.forms import ModelForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User 

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

YEARS = [x for x in range(2020,2030)]
# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

class EvaluationForm(forms.Form):
    first_Name = forms.CharField(label = "First Name", max_length = 200)
    last_Name = forms.CharField(label = "Last Name", max_length = 200)
    stud_id = forms.IntegerField(required = True, label = "Student ID")
    Evaluation_Number = forms.ChoiceField(label = "Evaluation Number: ", choices = EVALUATION_NUMBER)
    date = forms.DateField(label = "Date", initial = "2023-01-01", widget = forms.SelectDateWidget(years = YEARS))
    Pedagogy_A = forms.ChoiceField(label = "A. Focus for Learning: Standards and Objectives/Targets", choices = QUESTION_CHOICES)
    Pedagogy_B = forms.ChoiceField(label="B. Materials and Resources", choices = QUESTION_CHOICES)
    Pedagogy_C = forms.ChoiceField(label="C. Assessment of P-12 Learning", choices = QUESTION_CHOICES)
    Pedagogy_D = forms.ChoiceField(label="D. Differentiated Methods", choices = QUESTION_CHOICES)
    Pedagogy_E = forms.ChoiceField(label="E. Learning Target and Directions", choices = QUESTION_CHOICES)
    Pedagogy_F = forms.ChoiceField(label="F. Critical Thinking", choices = QUESTION_CHOICES)
    Pedagogy_G = forms.ChoiceField(label="G. Checking for Understanding and Adjusting", choices = QUESTION_CHOICES)
    Pedagogy_H = forms.ChoiceField(label="H. Digital Tools and Resources", choices = QUESTION_CHOICES)
    Pedagogy_I = forms.ChoiceField(label="I. Safe and Respectful Learning Enviornment", choices = QUESTION_CHOICES)
    Pedagogy_J = forms.ChoiceField(label="J. Data-Guided Instruction", choices = QUESTION_CHOICES)
    Pedagogy_K = forms.ChoiceField(label="K. Feedback to Learners", choices = QUESTION_CHOICES)
    Pedagogy_L = forms.ChoiceField(label="L. Assessment Techniques", choices = QUESTION_CHOICES)
    Pedagogy_M = forms.ChoiceField(label="M. Connections to Research and Theory", choices = QUESTION_CHOICES)
    Disposition_A = forms.ChoiceField(label="A. Participates in Professional Development (PD)", choices = QUESTION_CHOICES)
    Disposition_B = forms.ChoiceField(label="B. Demonstrates Effective Communication with Parents or Legal Guardians", choices = QUESTION_CHOICES)
    Disposition_C = forms.ChoiceField(label="C. Demonstrates Punctuality", choices = QUESTION_CHOICES)
    Disposition_D = forms.ChoiceField(label="D. Meets Deadlines and Obligations", choices = QUESTION_CHOICES)
    Disposition_E = forms.ChoiceField(label="E. Preparation", choices = QUESTION_CHOICES)
    Disposition_F = forms.ChoiceField(label="F. Collaboration", choices = QUESTION_CHOICES)
    Disposition_G = forms.ChoiceField(label="G. Advocacy to Meet the Needs of Learners or for the Teaching Profession", choices = QUESTION_CHOICES)
    Disposition_H = forms.ChoiceField(label="H. Responds Positively to Feedback and Constructive Criticism", choices = QUESTION_CHOICES)
    comment = forms.CharField(label="What went well? Areas of strength?", max_length = 1000)