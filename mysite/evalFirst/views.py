from django.shortcuts import render, redirect
from django.http import Http404
from django.template import loader
from django.http import HttpResponse
from .forms import EvaluationForm #CreateUserForm
from .models import Evaluation
from .models import Profile, User
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


from django.core.mail import EmailMessage
from datetime import datetime

# # Create your views here.

def emailSender(request):
    sendConfirmEmail(['sarahmcooney@gmail.com'], "Evaluation", "0001", "Sarah Cooney")
    sendNoticeEmail(['coon3571@ravens.benedictine.edu'], "0001")

def sendConfirmEmail(recipients, formType, submitID, sendTo):
    now = datetime.now()
    # mm/dd/YY H:M:S military time

    dt_string = now.strftime("%m/%d/%Y %H:%M:%S") #gets time
    msg = EmailMessage('No-reply Evaluation Submission Confirmation', "Hi", to = recipients)
    msg.send()

def sendNoticeEmail(recipients, submitID):
    msg = EmailMessage('No-reply Evaluation Submission Notification',
                    '''A new evaluation has been posted on your portal in the Raven's Student-Teacher Hub.
                    \n If you have any questions, please contact your supervisor.\n
                    \n submitID: ''' + submitID + '''\n
                    \n - Raven's Student-Teacher Hub''', to = recipients)
    msg.send()



def evaluationPage(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = EvaluationForm(response.POST)
            if form.is_valid():
                f = form.cleaned_data["first_Name"]
                l = form.cleaned_data["last_Name"]
                s = form.cleaned_data['portal_id']
                e = form.cleaned_data['Evaluation_Number']
                d = form.cleaned_data['date']
                q1a = form.cleaned_data['Pedagogy_A']
                q1b = form.cleaned_data['Pedagogy_B']
                q1c = form.cleaned_data['Pedagogy_C']
                q1d = form.cleaned_data['Pedagogy_D']
                q2e = form.cleaned_data['Pedagogy_E']
                q2f = form.cleaned_data['Pedagogy_F']
                q2g = form.cleaned_data['Pedagogy_G']
                q2h = form.cleaned_data['Pedagogy_H']
                q2i = form.cleaned_data['Pedagogy_I']
                q3j = form.cleaned_data['Pedagogy_J']
                q3k = form.cleaned_data['Pedagogy_K']
                q3l = form.cleaned_data['Pedagogy_L']
                q4m = form.cleaned_data['Pedagogy_M']
                q5a = form.cleaned_data['Disposition_A']
                q5b = form.cleaned_data['Disposition_B']
                q5c = form.cleaned_data['Disposition_C']
                q5d = form.cleaned_data['Disposition_D']
                q5e = form.cleaned_data['Disposition_E']
                q6f = form.cleaned_data['Disposition_F']
                q6g = form.cleaned_data['Disposition_G']
                q7h = form.cleaned_data['Disposition_H']
                com = form.cleaned_data["comment"]
                # u = form.cleaned_data['user']
                inquiry = Profile.objects.all()
                abool = 0
                for i in inquiry:
                    if i.student_ID == s:
                        su = User.objects.get(id=s)
                        abool = 1
                if abool == 0:
                    return HttpResponse("Please enter a real student id") #make a html template for this
                q = Evaluation(first_Name = f, last_Name = l, portal_id = s, Evaluation_Number = e, date = d, Pedagogy_A = q1a, Pedagogy_B = q1b, Pedagogy_C = q1c, Pedagogy_D = q1d, Pedagogy_E = q2e, Pedagogy_F = q2f, Pedagogy_G = q2g, Pedagogy_H = q2h, Pedagogy_I = q2i, Pedagogy_J = q3j, Pedagogy_K = q3k, Pedagogy_L = q3l, Pedagogy_M = q4m, Disposition_A = q5a, Disposition_B = q5b, Disposition_C = q5c, Disposition_D = q5d, Disposition_E = q5e, Disposition_F = q6f, Disposition_G = q6g, Disposition_H = q7h, comment = com, user=su)
                q.save()
                # emailSender(response)
            return render(response, "submissionSuccess.html", {"form":form})
        else:
            form = EvaluationForm()
        return render(response, "evalQuestions.html", {"form":form})
    else:
        messages.success(response, ("You must be logged in to view this page."))
        return redirect('login')


def listOfEvals(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=request.user.id)
        all_users = User.objects.all()
        all_evaluations = Evaluation.objects.all()
        template = loader.get_template('evalList.html')
        context = {
            'all_evaluations' : all_evaluations,
            'profile' : profile,
            'all_users' : all_users,
        }
        return HttpResponse(template.render(context, request))
    else:
        messages.success(request, ("You must be logged in to view this page."))
        return redirect('login')

def evaluationDetails(request, stud_id):
    try:
        eval = Evaluation.objects.get(id=stud_id)
        template = loader.get_template('evaluationDetails.html')
        context = {
            'eval' : eval,
        }
    except Evaluation.DoesNotExist:
        raise Http404("Evaluation does not exist")
    return HttpResponse(template.render(context, request))

def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("You must be logged in to view this page."))
        return redirect('login')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        evaluations = Evaluation.objects.filter(user_id=pk)
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
