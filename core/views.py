from django.shortcuts import render
from dashboard.models import JobPostModel
from dashboard.contains import JOB_TYPE

def home(request):
    job_list = JobPostModel.objects.all()

    search_item = request.GET.get('search')
    job = request.GET.get('job')
    if search_item:
        job_list = JobPostModel.objects.filter(title__icontains = search_item)
    elif job == 'All':
        job_list = JobPostModel.objects.all()
    elif job:
        job_list = JobPostModel.objects.filter(job_type = job)


    job_type = ['All']
    for item  in JOB_TYPE:
        print(item)
        job_type.append(item[0])

    return render(request, 'home.html', {'data': job_list, 'job_type': job_type})
