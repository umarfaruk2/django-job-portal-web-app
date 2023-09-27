from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import JobPostModel
from django.views.generic.edit import UpdateView
from .forms import JobPostModelForm
from candidate.models import MyAppliedJobModel

def job_post(request):
    if request.method == 'POST':
        fm = JobPostModelForm(request.POST)        
        if fm.is_valid():
            fm.instance.user = request.user
            fm.save()
            return redirect('posted_job')
    else:
        fm = JobPostModelForm()
    return render(request, 'dashboard/job_post.html', {'form': fm})

# my posted jobs
def posted_job(request):
    jobs = JobPostModel.objects.filter(user = request.user)
    return render(request, 'dashboard/posted_jobs.html', {'data': jobs})

def applied_job(request):
    apply_post = MyAppliedJobModel.objects.filter(jobPost__user = request.user)
    return render(request, 'dashboard/applied_jobs.html', {'data': apply_post})

class UpdateJob(UpdateView):
    template_name = 'dashboard/update_job.html' 
    model = JobPostModel
    form_class = JobPostModelForm
    success_url = reverse_lazy('posted_job') 

def delete_post(request, id):
    JobPostModel.objects.get(pk = id).delete() 
    return redirect('posted_job')

def delete_candidate_apply(request, id):
    MyAppliedJobModel.objects.get(pk = id).delete()   

    return redirect('applied_job')