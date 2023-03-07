from django.shortcuts import render, redirect
from django.http import HttpResponse
from evalFirst.models import Profile
from django.contrib import messages

def homePage(request):
    if request.user.is_authenticated:
        return render(request, 'studentHomePage.html')
    else:
        messages.success(request, ("You must be logged in to view this page."))
        return redirect('login')
    
# Create your views here.