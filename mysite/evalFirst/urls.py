from django.urls import path

from . import views

urlpatterns = [
    path('questions/', views.evaluationPage, name='evaluationPage'),
    path('questions/list', views.listOfEvals, name='listOfEvals'),
]