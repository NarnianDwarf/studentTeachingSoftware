from django.db import models

# Create your models here.
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

class submitAttendance(models.Model):
    fname = models.CharField(max_length = 200, default = "Enter First Name")
    lname = models.CharField(max_length = 200, default = "Enter Last Name")
    stud_id = models.IntegerField(default = 0)
    date = models.DateField()
    # attend = models.IntegerField(choices = ATTENDANCE_CHOICES, default = 0)
    reason = models.CharField(max_length = 1000, default = "")