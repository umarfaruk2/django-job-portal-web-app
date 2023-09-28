from django.contrib import admin
from .models import PaymentGateWaySettings, PricePlanModel

admin.site.register(PaymentGateWaySettings)
admin.site.register(PricePlanModel)