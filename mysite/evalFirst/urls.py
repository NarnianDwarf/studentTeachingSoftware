from django.urls import path

from . import views

urlpatterns = [
    path('', views.evaluationPage, name='evaluationPage'),
    path('questions/', views.evaluationPage, name='questionsPage'),
    path('list/trying', views.listOfEvals, name='listOfEvals'),
]