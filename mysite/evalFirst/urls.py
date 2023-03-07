from django.urls import path

from . import views

urlpatterns = [
    path('questions/', views.evaluationPage, name='evaluationPage'),
    path('questions/list', views.listOfEvals, name='listOfEvals'),
    path('<int:stud_id>', views.evaluationDetails, name='evaluationDetails'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name="profile"),
    # path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    # path('', views.loginPage, name='login2'),
    path('logout', views.logoutUser, name='logout'),
]