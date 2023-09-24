from django.contrib import admin
from .models import JobPostModel

@admin.register(JobPostModel)
class JobPostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'company', 'location', 'salary', 'description', 'publish_date')
    