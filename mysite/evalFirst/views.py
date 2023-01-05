from django.shortcuts import render
from django.http import HttpResponse

def evaluationPage(request):
    return render(request, 'evaluation.html')
# Create your views here.
