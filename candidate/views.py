from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from dashboard.models import JobPostModel
from .models import CandidateModel, MyAppliedJobModel
from .forms import CandidateModelForm
from accounts.models import RegisterInfoModel
from django.views.generic.edit import UpdateView
from django.contrib import messages

def job_detail(request, id):
    get_job = JobPostModel.objects.get(pk = id)

    return render(request, 'candidate/job_detail.html', {'data': get_job})

def create_profile(request):
    if request.method == 'POST':
        fm = CandidateModelForm(request.POST)
        if fm.is_valid():
            fm.instance.user = request.user
            fm.save() 
            return redirect('profile') 
    else:
        fm = CandidateModelForm()
    return render(request, 'candidate/create_profile.html', {'form': fm})
        

def profile(request):
    profile = None
    try:
        profile = CandidateModel.objects.get(user = request.user) 
    except:
        print('no data')

    return render(request, 'candidate/profile.html', {'data': profile})

class UpdateProfile(UpdateView):
    template_name = 'candidate/update_profile.html' 
    model = CandidateModel
    form_class = CandidateModelForm
    success_url = reverse_lazy('profile') 
    
def apply_job(request, id):
    if request.user.is_authenticated:
        register_u = None
        try:
            candidate = CandidateModel.objects.get(user = request.user)
            jobPost = JobPostModel.objects.get(pk = id)
            
            register_u = RegisterInfoModel.objects.get(user = request.user)
            try:
                check = MyAppliedJobModel.objects.get(jobPost__id = id, user = request.user)
                messages.error(request, 'You already apply for this post')
            except:
                apply_job = MyAppliedJobModel.objects.create(user = request.user, candidate = candidate, jobPost = jobPost)
                messages.success(request, 'Apply Successfully!')
        except:
            if register_u == None:
                messages.error(request, "Your not a candidate")
            else:
                    messages.error(request, 'Create Your profile first')
        return redirect('job_detail', id = id)
    else:
        return redirect('login')

    