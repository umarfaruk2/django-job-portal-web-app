from django.contrib import admin
from .models import RegisterInfoModel


@admin.register(RegisterInfoModel)
class RegisterModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company', 'candidate')
    
