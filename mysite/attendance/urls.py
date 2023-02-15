from django.urls import path

from . import views

urlpatterns = [
    path('', views.attendancePage, name='attendancePage'),
]