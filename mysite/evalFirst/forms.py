from django import forms

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

class firstEvaluationForm(forms.Form):
    fname = forms.CharField(label = "First Name", max_length = 200)
    lname = forms.CharField(label = "Last Name", max_length = 200)
    stud_id = forms.IntegerField(required = True, label = "Student ID")
    question1a = forms.ChoiceField(label = "A. Focus for Learning: Standards and Objectives/Targets", choices = QUESTION_CHOICES)
    question1b = forms.ChoiceField(label="B. Materials and Resources", choices = QUESTION_CHOICES)
    question1c = forms.ChoiceField(label="C. Assessment of P-12 Learning", choices = QUESTION_CHOICES)
    question1d = forms.ChoiceField(label="D. Differentiated Methods", choices = QUESTION_CHOICES)
    question2e = forms.ChoiceField(label="E. Learning Target and Directions", choices = QUESTION_CHOICES)
    question2f = forms.ChoiceField(label="F. Critical Thinking", choices = QUESTION_CHOICES)
    question2g = forms.ChoiceField(label="G. Checking for Understanding and Adjusting", choices = QUESTION_CHOICES)
    question2h = forms.ChoiceField(label="H. Digital Tools and Resources", choices = QUESTION_CHOICES)
    question2i = forms.ChoiceField(label="I. Safe and Respectful Learning Enviornment", choices = QUESTION_CHOICES)
    question3j = forms.ChoiceField(label="J. Data-Guided Instruction", choices = QUESTION_CHOICES)
    question3k = forms.ChoiceField(label="K. Feedback to Learners", choices = QUESTION_CHOICES)
    question3l = forms.ChoiceField(label="L. Assessment Techniques", choices = QUESTION_CHOICES)
    question4m = forms.ChoiceField(label="M. Connections to Research and Theory", choices = QUESTION_CHOICES)
    question5a = forms.ChoiceField(label="A. Participates in Professional Development (PD)", choices = QUESTION_CHOICES)
    question5b = forms.ChoiceField(label="B. Demonstrates Effective Communication with Parents or Legal Guardians", choices = QUESTION_CHOICES)
    question5c = forms.ChoiceField(label="C. Demonstrates Punctuality", choices = QUESTION_CHOICES)
    question5d = forms.ChoiceField(label="D. Meets Deadlines and Obligations", choices = QUESTION_CHOICES)
    question5e = forms.ChoiceField(label="E. Preparation", choices = QUESTION_CHOICES)
    question6f = forms.ChoiceField(label="F. Collaboration", choices = QUESTION_CHOICES)
    question6g = forms.ChoiceField(label="G. Advocacy to Meet the Needs of Learners or for the Teaching Profession", choices = QUESTION_CHOICES)
    question7h = forms.ChoiceField(label="H. Responds Positively to Feedback and Constructive Criticism", choices = QUESTION_CHOICES)
    comment = forms.CharField(label="What went well? Areas of strength?", max_length = 1000)