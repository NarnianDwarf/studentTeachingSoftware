from django.contrib import admin
from django.contrib.auth.models import User
from .models import firstEvaluation, Profile
from import_export import resources
# from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]


admin.site.unregister(User)
#COULD THIS BE THE ISSUE????
admin.site.register(User, UserAdmin)


# class FirstEvaluationResource(resources.ModelResource):
#     # full_title = Field()

#     class Meta:
#         model = firstEvaluation

#     def dehydrate_full_title(self):
#         first_name = getattr(firstevaluation.fname, "name", "unknown")
#         last_name = getattr(firstevaluation.lname, "name", "unknown")
#         stud = getattr(firstevaluation.stud_id, "Id", "unknown")
#         return '%s %s - %s' % (first_name, last_name, stud)

# class FirstEvaluationAdmin(ExportActionMixin, admin.ModelAdmin):
#     # resources_classes = [FirstEvaluationResource]
#     First_Name = getattr(firstEvaluation, "fname")
#     Last_Name = getattr(firstEvaluation, "lname")
#     Student_ID = getattr(firstEvaluation, "stud_id")
#     list_display = ('First_Name', 'Last_Name', 'Student_ID')

def name(obj):
    return("%s, %s" % (obj.last_Name, obj.first_Name))

def date_submitted(obj):
    return("%s" % (obj.date))

class FirstEvaluationAdmin(ImportExportModelAdmin):
    model = firstEvaluation
    list_display = (name, date_submitted)

def export_selected_objects(modeladmin, request, queryset):
    selected = queryset.values_list('pk', flat=True)
    ct = ContentType.objects.get_for_model(queryset.model)
    # return HttpResponseRedirect('/export/?ct=%s&ids=%s' % (
    #     ct.pk,
    #     ','.join(str(pk) for pk in selected),
    # ))

admin.site.add_action(export_selected_objects)
admin.site.register(firstEvaluation, FirstEvaluationAdmin)
# admin.site.register(firstEvaluation)
# admin.site.register(Profile)

#mix user and profile info


#TWO IDEAS:

#1. I make a value that is a student id associated with each user
#2. I make a dropdown list of users????



