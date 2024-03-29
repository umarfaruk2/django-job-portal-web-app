from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from dashboard.models import JobPostModel
from .models import CandidateModel, MyAppliedJobModel
from .forms import CandidateModelForm
from accounts.models import RegisterInfoModel
from django.views.generic.edit import UpdateView
from django.contrib import messages
from price_plan.models import PricePlanModel
from django.http import Http404

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

def apply_job_list(request):
    my_job_list = MyAppliedJobModel.objects.filter(user = request.user)
    return render(request, 'candidate/apply_job_list.html', {'data': my_job_list})

def delete_apply_job(request, id):
    MyAppliedJobModel.objects.get(pk = id).delete()

    return redirect('apply_job_list')

class UpdateProfile(UpdateView):
    template_name = 'candidate/update_profile.html' 
    model = CandidateModel
    form_class = CandidateModelForm
    success_url = reverse_lazy('profile') 
    

def apply_job(request, id):
    if request.user.is_authenticated:
        register_u = None
        candidate = None
        jobPost = None
        
        register_u = RegisterInfoModel.objects.get(user = request.user)
        print(register_u)
        if not register_u.candidate:
            messages.error(request, "Your not a candidate")
        else:
            try:
                candidate = CandidateModel.objects.get(user = request.user)
                jobPost = JobPostModel.objects.get(id = id)
                
                try:
                    check = MyAppliedJobModel.objects.get(jobPost__id = id, user = request.user)
                    messages.error(request, 'You already apply for this post')
                except:
                    total_job = MyAppliedJobModel.objects.filter(user = request.user).count()
                    price_plan = PricePlanModel.objects.get(user = request.user)
                    print('price_plan...', price_plan)
                    if total_job >= 20 and price_plan.plan == 'Free':
                        messages.error(request, "You can't apply over 20 job for this month with Free plan. Please update you plan")
                    elif total_job >= 50 and price_plan.plan == 'Basic':
                        messages.error(request, "You can't apply over 50 job for this month with Basic plan. Please update you plan")
                    elif total_job >= 150 and price_plan.plan == 'Premium':
                        messages.error(request, "You can't apply over 150 job for this month with Premium plan.")
                    else:
                        apply_job = MyAppliedJobModel.objects.create(user = request.user, candidate = candidate, jobPost = jobPost)
                        messages.success(request, 'Apply Successfully!')
                        
            except:
                messages.error(request, 'Create Your profile first')
                 
        return redirect('job_detail', id = id)
    else:
        return redirect('login')