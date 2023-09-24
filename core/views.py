from django.shortcuts import render
from dashboard.models import JobPostModel

def home(request):
    job_list = JobPostModel.objects.all()

    return render(request, 'home.html', {'data': job_list})