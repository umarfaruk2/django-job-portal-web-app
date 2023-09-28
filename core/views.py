from django.shortcuts import render, HttpResponse
from dashboard.models import JobPostModel
from dashboard.contains import JOB_TYPE
from price_plan.models import PricePlanModel

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
    
    if request.COOKIES.get('price_plan'):
        try:
            find_plan = PricePlanModel.objects.get(user = request.user)    
            find_plan.plan = request.COOKIES.get('price_plan', None)
            find_plan.save()
        except PricePlanModel.DoesNotExist:
            create_plan = PricePlanModel.objects.create(user = request.user, plan = request.COOKIES.get('price_plan', None))
        
    job_type = ['All']

    for item  in JOB_TYPE:
        job_type.append(item[0])

    return render(request, 'home.html', {'data': job_list, 'job_type': job_type}) 
