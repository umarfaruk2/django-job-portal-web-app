from django.db import models
from accounts.models import RegisterInfoModel
from dashboard.models import JobPostModel


class CandidateModel(models.Model):
    SKILLS = (
        ('Javascript', 'Javascript'),
        ('React', 'React'),
        ('Django', 'Django'),
        ('Python', 'Python'),
        ('MySql', 'MySql'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS')
    )
    user = models.OneToOneField(RegisterInfoModel, on_delete=models.CASCADE)
    jobPost = models.ForeignKey(JobPostModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=70, unique=True)
    about = models.TextField(max_length=150)
    phone = models.CharField(max_length=20)
    skill = models.CharField(choices=SKILLS, max_length=20) 

    def __str__(self):
        return self.name
