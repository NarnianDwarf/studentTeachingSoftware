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
    question2 = forms.ChoiceField(label="Materials and Resources", choices = QUESTION_CHOICES)
    question3 = forms.ChoiceField(label="Assessment of P-12 Learning", choices = QUESTION_CHOICES)
    question4 = forms.ChoiceField(label="Differentiated Methods", choices = QUESTION_CHOICES)
    question5 = forms.ChoiceField(label="Learning Target and Directions", choices = QUESTION_CHOICES)
    question6 = forms.ChoiceField(label="Critical Thinking", choices = QUESTION_CHOICES)
    question7 = forms.ChoiceField(label="Checking for Understanding and Adjusting", choices = QUESTION_CHOICES)
    question8 = forms.ChoiceField(label="Digital Tools and Resources", choices = QUESTION_CHOICES)
    question9 = forms.ChoiceField(label="Safe and Respectful Learning Enviornment", choices = QUESTION_CHOICES)
    question10 = forms.ChoiceField(label="Data-Guided Instruction", choices = QUESTION_CHOICES)
    question11 = forms.ChoiceField(label="Feedback to Learners", choices = QUESTION_CHOICES)
    question12 = forms.ChoiceField(label="Assessment Techniques", choices = QUESTION_CHOICES)
    question13 = forms.ChoiceField(label="Connections to Research and Theory", choices = QUESTION_CHOICES)
    question14 = forms.ChoiceField(label="Participates in Professional Development (PD)", choices = QUESTION_CHOICES)
    question15 = forms.ChoiceField(label="Demonstrates Effective Communication with Parents or Legal Guardians", choices = QUESTION_CHOICES)
    question16 = forms.ChoiceField(label="Demonstrates Punctuality", choices = QUESTION_CHOICES)
    question17 = forms.ChoiceField(label="Meets Deadlines and Obligations", choices = QUESTION_CHOICES)
    question18 = forms.ChoiceField(label="Preparation", choices = QUESTION_CHOICES)
    question19 = forms.ChoiceField(label="Collaboration", choices = QUESTION_CHOICES)
    question20 = forms.ChoiceField(label="Advocacy to Meet the Needs of Learners or for the Teaching Profession", choices = QUESTION_CHOICES)
    question21 = forms.ChoiceField(label="Responds Positively to Feedback and Constructive Criticism", choices = QUESTION_CHOICES)
    # At the end of the form, there is a blank box asking for what went well and areas of strength which I did not include here.
