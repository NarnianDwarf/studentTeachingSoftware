from django.contrib import admin
from django.contrib.auth.models import User
from .models import firstEvaluation, Profile

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]


admin.site.unregister(User)
#COULD THIS BE THE ISSUE????
admin.site.register(User, UserAdmin)
admin.site.register(firstEvaluation)
# admin.site.register(Profile)

#mix user and profile info


#TWO IDEAS:

#1. I make a value that is a student id associated with each user
#2. I make a dropdown list of users????



