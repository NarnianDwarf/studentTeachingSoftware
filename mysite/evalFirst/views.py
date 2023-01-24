from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import firstEvaluationForm, firstQuestionsForm
from .models import firstEvaluation, firstQuestions

# Create your views here.

def evaluationPage(response):
    if response.method == "POST":
        form = firstEvaluationForm(response.POST)

        if form.is_valid():
            fn = form.cleaned_data["first_name"]
            ln = form.cleaned_data["last_name"]
            sid = form.cleaned_data['student_id']
            t = firstEvaluation(first_name = fn, last_name = ln, student_id = sid)
            t.save()
        
        return render(response, "evalQuestions.html", {"form":form})
    else:
        form = firstEvaluationForm()
    return render(response, "firstEvaluation.html", {"form":form})

# def questionsPage(response, id):
def questionsPage(response):
    # q = firstEvaluation.objects.get(id=id)

    if response.method == "POST":
        form = firstQuestionsForm(response.POST)

        if form.is_valid():
            fn = form.cleaned_data["first_name"]
            ln = form.cleaned_data["last_name"]
            sid = form.cleaned_data['student_id']
            q1 = form.cleaned_data['question1']
            q2 = form.cleaned_data['question2']
            q3 = form.cleaned_data['question3']
            q4 = form.cleaned_data['question4']
            q5 = form.cleaned_data['question5']
            q6 = form.cleaned_data['question6']
            q7 = form.cleaned_data['question7']
            q8 = form.cleaned_data['question8']
            q9 = form.cleaned_data['question9']
            q10 = form.cleaned_data['question10']
            q11 = form.cleaned_data['question11']
            q12 = form.cleaned_data['question12']
            q13 = form.cleaned_data['question13']
            q14 = form.cleaned_data['question14']
            q15 = form.cleaned_data['question15']
            q16 = form.cleaned_data['question16']
            q17 = form.cleaned_data['question17']
            q18 = form.cleaned_data['question18']
            q19 = form.cleaned_data['question19']
            q20 = form.cleaned_data['question20']
            q21 = form.cleaned_data['question21']
            com = form.cleaned_data["comment"]
            q.firstQuestion(first_name = fn, last_name = ln, student_id = sid, question1 = q1, question2 = q2, question3 = q3, question4 = q4, question5 = q5, question6 = q6, question7 = q7, question8 = q8, question9 = q9, question10 = q10, question11 = q11, question12 = q12, question13 = q13, question14 = q14, question15 = q15, question16 = q16, question17 = q17, question18 = q18, question19 = q19, question20 = q20, question21 = q21, comment = com)
            q.save()
        
        return render(response, "submissionSuccess.html")
    else:
        form = firstQuestionsForm()
    return render(response, "evalQuestions.html", {"form":form})
    # return render(response, "evalQuestions.html", {"q":q})

def listOfEvals(request):
    all_evaluations = firstEvaluation.objects.all()
    template = loader.get_template('/evalList.html')
    context = {
        'all_evaluations' : all_evaluations,
    }
    return HttpResponse(template.render(context, request))