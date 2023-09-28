from django.db import models
from django.contrib.auth.models import User

class PaymentGateWaySettings(models.Model):
    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null = True)

class PricePlanModel(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE) 
   plan = models.CharField(max_length=10)

   def __str__(self):
       return self.plan