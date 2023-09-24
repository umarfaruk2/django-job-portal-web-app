from django.db import models
from django.contrib.auth.models import User


class RegisterInfoModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.BooleanField(default=False)
    candidate = models.BooleanField(default=False)