from django.db import models
from django.contrib.auth.models import User
from accounts.models import RegisterInfoModel


class JobPostModel(models.Model):
    JOB_TYPE = (
        ('FULL-TIME', 'FULL-TIME'),
        ('PART-TIME', 'PART-TIME')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    job_type = models.CharField(choices=JOB_TYPE, max_length=50)
    salary = models.IntegerField()
    description = models.TextField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title