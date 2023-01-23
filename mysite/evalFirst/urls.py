from django.urls import path

from . import views

urlpatterns = [
    path('', views.evaluationPage, name='evaluationPage'),
    path('questions/', views.questionsPage, name='questionsPage'),
]