from django.shortcuts import render
from django.http import HttpResponse
from .forms import firstEvaluationForm

# Create your views here.

def evaluationPage(response):
    if response.method == "POST":
        form = firstEvaluationForm(response.POST)

        if form.is_valid():
            fn = form.cleaned_data["first_name"]
            ln = form.cleaned_data["last_name"]
            sid = form.cleaned_data["student_id"]
            t = firstEvaluation(first_name = fn, last_name = ln, student_id = sid)
            t.save()
        
        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = firstEvaluationForm()
        context = {"form":form}
    return render(response, "firstEvaluation.html", context)

