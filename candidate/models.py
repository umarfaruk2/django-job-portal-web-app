from django.db import models
from dashboard.models import JobPostModel
from django.contrib.auth.models import User
from accounts.models import RegisterInfoModel


class CandidateModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=70, unique=True)
    about = models.TextField(max_length=150)
    phone = models.CharField(max_length=20)
    education = models.CharField(max_length=50, default=None) 

    def __str__(self):
        return self.name


class MyAppliedJobModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    candidate = models.ForeignKey(CandidateModel, on_delete=models.CASCADE)
    jobPost = models.ForeignKey(JobPostModel, on_delete=models.CASCADE)



