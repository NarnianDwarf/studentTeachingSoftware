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
admin.site.register(User, UserAdmin)
admin.site.register(firstEvaluation)
# admin.site.register(Profile)

#mix user and profile info




