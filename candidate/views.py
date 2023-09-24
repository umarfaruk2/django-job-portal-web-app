from django.shortcuts import render
from dashboard.models import JobPostModel

def job_detail(request, id):
    get_job = JobPostModel.objects.get(pk = id)

    return render(request, 'candidate/job_detail.html', {'data': get_job})