from django.shortcuts import render
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from .forms import attendanceForm
from .models import submitAttendance

# Create your views here.

def attendancePage(response):
    if response.method == "POST":
        form = attendanceForm(response.POST)
        if form.is_valid():
            f = form.cleaned_data["fname"]
            l = form.cleaned_data["lname"]
            s = form.cleaned_data['stud_id']
            d = form.cleaned_data['date']
            # a = form.cleaned_data['attend']
            r = form.cleaned_data["reason"]
            
            q = submitAttendance(fname = f, lname = l, stud_id = s, date = d, reason = r)
            q.save()
        return render(response, "attendanceSubmission.html", {"form":form})
    else:
        form = attendanceForm()
    return render(response, "attendance.html", {"form":form})