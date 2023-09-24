from django import forms
from .models import JobPostModel


class JobPostModelForm(forms.ModelForm):
    class Meta:
        model = JobPostModel
        fields = ['title', 'company', 'location', 'job_type', 'salary', 'description']