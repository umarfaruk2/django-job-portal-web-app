from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('price_plan/', views.price_plan, name='price_plan'),
    path('buy_plan/<slug:plan>', views.buy_plan, name='buy_plan'),
    path('success/', views.success_view, name='success'),
    path('faild/', views.faild_view, name='faild'),
    path('free_plan/', views.free_plan, name='free_plan'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
