from django.shortcuts import render, redirect
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from .forms import firstEvaluationForm #CreateUserForm
from .models import firstEvaluation
from .models import Profile
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def evaluationPage(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = firstEvaluationForm(response.POST)
            if form.is_valid():
                f = form.cleaned_data["fname"]
                l = form.cleaned_data["lname"]
                s = form.cleaned_data['stud_id']
                q1a = form.cleaned_data['question1a']
                q1b = form.cleaned_data['question1b']
                q1c = form.cleaned_data['question1c']
                q1d = form.cleaned_data['question1d']
                q2e = form.cleaned_data['question2e']
                q2f = form.cleaned_data['question2f']
                q2g = form.cleaned_data['question2g']
                q2h = form.cleaned_data['question2h']
                q2i = form.cleaned_data['question2i']
                q3j = form.cleaned_data['question3j']
                q3k = form.cleaned_data['question3k']
                q3l = form.cleaned_data['question3l']
                q4m = form.cleaned_data['question4m']
                q5a = form.cleaned_data['question5a']
                q5b = form.cleaned_data['question5b']
                q5c = form.cleaned_data['question5c']
                q5d = form.cleaned_data['question5d']
                q5e = form.cleaned_data['question5e']
                q6f = form.cleaned_data['question6f']
                q6g = form.cleaned_data['question6g']
                q7h = form.cleaned_data['question7h']
                com = form.cleaned_data["comment"]

                q = firstEvaluation(user=response.user, fname = f, lname = l, stud_id = s, question1a = q1a, question1b = q1b, question1c = q1c, question1d = q1d, question2e = q2e, question2f = q2f, question2g = q2g, question2h = q2h, question2i = q2i, question3j = q3j, question3k = q3k, question3l = q3l, question4m = q4m, question5a = q5a, question5b = q5b, question5c = q5c, question5d = q5d, question5e = q5e, question6f = q6f, question6g = q6g, question7h = q7h, comment = com)
                q.save()
            return render(response, "submissionSuccess.html", {"form":form})
        else:
            form = firstEvaluationForm()
        return render(response, "evalQuestions.html", {"form":form})
    else:
        messages.success(response, ("You must be logged in to view this page."))
        return redirect('login')

def listOfEvals(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.id)
        all_evaluations = firstEvaluation.objects.all()
        template = loader.get_template('evalList.html')
        context = {
            'all_evaluations' : all_evaluations,
            'profile' : profile,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.success(request, ("You must be logged in to view this page."))
        return redirect('login')

def evaluationDetails(request, stud_id):
    try:
        eval = firstEvaluation.objects.get(id=stud_id)
        template = loader.get_template('evaluationDetails.html')
        context = {
            'eval' : eval,
        }
    except firstEvaluation.DoesNotExist:
        raise Http404("Evaluation does not exist")
    return HttpResponse(template.render(context, request))

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("You must be loggined in beech."))
        return redirect('login')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        evaluations = firstEvaluation.objects.filter(user_id=pk)
        return render(request, "profile.html", {"profile": profile, "evaluations": evaluations})
    else:
        messages.success(request, ("You must be logged in to view this page."))
        return redirect('login')

# def registerPage(request):
#     form = CreateUserForm()

#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user = form.cleaned_data.get('username')

#             messages.success(request, 'Account was created for '+ user)
#             return redirect('login')

#     template = loader.get_template('register.html')
#     context = {'form': form}
#     return HttpResponse(template.render(context, request))

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('homeFromLogin/')
        else:
            messages.info(request, 'Username or password is incorrect.')

    template = loader.get_template('login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logoutUser(request):
    logout(request)
    return redirect('login')
