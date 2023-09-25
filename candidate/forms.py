from django import forms
from .models import CandidateModel


class CandidateModelForm(forms.ModelForm):
    class Meta:
        model = CandidateModel
        fields = ['name', 'email', 'about', 'phone', 'education']
        