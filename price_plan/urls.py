from django.urls import path
from . import views

urlpatterns = [
    path('price_plan/', views.price_plan, name='price_plan'),
    path('buy_plan/<slug:plan>', views.buy_plan, name='buy_plan'),
    path('success/', views.success_view, name='success'),
    path('faild/', views.faild_view, name='faild'),
]
