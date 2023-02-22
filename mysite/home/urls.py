from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('evaluationPage', include ('evalFirst.urls')),
    path('firstEvaluation/', include('evalFirst.urls')),

]