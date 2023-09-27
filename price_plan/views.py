from django.shortcuts import render, redirect
from django.http import HttpResponse
from .ssl import sslcommerz_payment_gateway
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from accounts.models import RegisterInfoModel

def price_plan(request):
    return render(request, 'price_plan/price_plan.html')


def buy_plan(request, plan):
    if request.user.is_authenticated: 
        data = RegisterInfoModel.objects.get(user = request.user)   
        if data.candidate:
            if plan == 'basic':
                return redirect(sslcommerz_payment_gateway(request, 'basic', str(request.user.id), 1999))
            else:
                return redirect(sslcommerz_payment_gateway(request, 'premium', str(request.user.id), 4999))
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
    
    request.session['payment_plan'] = plan
    # response = HttpResponse('success')
    # response.set_cookie('payment_plan', plan) 
    
    messages.success(request, f"Payment done successfully for {data['value_b']}")
    return redirect('home')

    