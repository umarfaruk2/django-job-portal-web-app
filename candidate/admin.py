from django.contrib import admin
from .models import CandidateModel, MyAppliedJobModel

@admin.register(CandidateModel)
class CandidateModelForm(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email', 'phone', 'about', 'education')


@admin.register(MyAppliedJobModel)
class MyApplyJobModelForm(admin.ModelAdmin):
    list_display = ('user', 'candidate', 'jobPost')