from django.contrib import admin
from django.contrib.auth.models import User
from .models import Evaluation, Profile
from import_export import resources
# from import_export.admin import ExportActionMixin
from import_export.admin import ImportExportModelAdmin
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
# from .export import export_as_xls

# class MyAdmin(admin.ModelAdmin):
#     actions = [export_as_xls]
# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInline]


admin.site.unregister(User)
#COULD THIS BE THE ISSUE????
admin.site.register(User, UserAdmin)

# THESE WERE THE DIFFERENT WAYS WE TRIED TO GET THE ADMIN SITE TO ONLY EXPORT SELECTED EVALUATIONS

# class EvaluationResource(resources.ModelResource):
#     # full_title = Field()

#     class Meta:
#         model = Evaluation

#     def __init__(self, form_fields=None):
#         super().__init__()
#         self.form_fields = form_fields
    
#     def get_export_fields(self):
#         return [self.fields[f] for f in self.form_fields]
    
# def export_selected_objects(modeladmin, request, queryset):
#     selected = queryset.values_list('pk', flat=True)
#     ct = Evaluation.objects.get_for_model(queryset.model)
#     return HttpResponseRedirect('export/?user_id=%s' % (
#         # ct.pk,
#         ','.join(str(pk) for pk in selected),
#     ))

    # def dehydrate_full_title(self):
    #     first_name = getattr(evaluation.fname, "name", "unknown")
    #     last_name = getattr(evaluation.lname, "name", "unknown")
    #     stud = getattr(evaluation.stud_id, "Id", "unknown")
    #     return '%s %s - %s' % (first_name, last_name, stud)

# class EvaluationAdmin(ExportActionMixin, admin.ModelAdmin):
#     # resources_classes = [EvaluationResource]
#     First_Name = getattr(Evaluation, "fname")
#     Last_Name = getattr(Evaluation, "lname")
#     Student_ID = getattr(Evaluation, "stud_id")
#     list_display = ('First_Name', 'Last_Name', 'Student_ID')

def name(obj):
    return("%s, %s" % (obj.last_Name, obj.first_Name))

def date_submitted(obj):
    return("%s" % (obj.date))

def evaluation_number(obj):
    return("%s" % (obj.Evaluation_Number))

class EvaluationAdmin(ImportExportModelAdmin):
    model = Evaluation
    list_display = (name, date_submitted, evaluation_number)
    # list_filter = ['date']
    # resource_class = EvaluationResource

    # def get_export_resource_kwargs(self, request, *args, **kwargs):
    #     formats = self.get_export_formats()
    #     # form = EvaluationExportForm(formats, request.POST or None)
    #     form_fields = ("First_Name",)
    #     return {"forms_fields": form_fields}

    # https://docs.djangoproject.com/en/4.1/ref/models/options/
    # ordering = [Evaluation('last_Name')]
    # Evaluation.objects.all().order_by('Evaluation_Number', 'date', 'last_Name').values()
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     qs = qs.annotate(models.Count('order'))
    #     return qs
    # def number



# admin.site.add_action(export_selected_objects)
admin.site.register(Evaluation, EvaluationAdmin)
# admin.site.register(Evaluation)
# admin.site.register(Profile)

#mix user and profile info


#TWO IDEAS:

#1. I make a value that is a student id associated with each user
#2. I make a dropdown list of users????



