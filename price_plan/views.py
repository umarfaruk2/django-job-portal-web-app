from django.shortcuts import render, redirect
from django.http import HttpResponse
from .ssl import sslcommerz_payment_gateway
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import RegisterInfoModel
from .models import PricePlanModel

def price_plan(request):
    return render(request, 'price_plan/price_plan.html')


def buy_plan(request, plan):
    if request.user.is_authenticated: 
        data = RegisterInfoModel.objects.get(user = request.user)   
        if data.candidate:
            if plan == 'Basic':
                return redirect(sslcommerz_payment_gateway(request, 'Basic', str(request.user.id), 1999))
            else:
                return redirect(sslcommerz_payment_gateway(request, 'Premium', str(request.user.id), 4999))
        else:
            messages.error(request, 'This plans for only candidate')
            return redirect('price_plan')
    else:
        return redirect('login')

@method_decorator(csrf_exempt, name='dispatch')
def faild_view(request):
    messages.error(request, 'Payment faild !')
    return redirect('home')

@method_decorator(csrf_exempt, name='dispatch')
def success_view(request):
    data = request.POST
    plan = data.get('value_b')  

    response = redirect('home')
    response.set_cookie('price_plan', plan, max_age=3600)

    messages.success(request, f"Payment done successfully for {data['value_b']}")
    return response

def free_plan(request):
    if request.user.is_authenticated: 
        data = RegisterInfoModel.objects.get(user = request.user)   
        if data.candidate:
            price_plan = PricePlanModel.objects.get(user = request.user)    
            price_plan.plan = 'Free'
            price_plan.save()
            response = redirect('price_plan')
            response.set_cookie('price_plan', 'Free', max_age=3600)
            return response
        else:
            messages.error(request, 'This plans for only candidate')
            return redirect('price_plan')
    else:
        return redirect('login')