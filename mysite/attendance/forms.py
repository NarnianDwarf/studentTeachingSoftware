from django import forms

NONE = None
PRESENT = 2
LATE = 1
ABSENT = 0
    
ATTENDANCE_CHOICES = (
    (NONE, "----------"),
    (PRESENT, 'Present'),
    (LATE, 'Late'),
    (ABSENT, 'Absent'),
)

class attendanceForm(forms.Form):
    fname = forms.CharField(label = "First Name", max_length = 200)
    lname = forms.CharField(label = "Last Name", max_length = 200)
    stud_id = forms.IntegerField(required = True, label = "Student ID")
    date = forms.DateField(label = "Date (mm-dd-yyyy)")
    attend = forms.ChoiceField(label = "Please Mark Your Attendance", choices = ATTENDANCE_CHOICES)