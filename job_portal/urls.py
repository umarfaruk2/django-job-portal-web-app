from django.contrib import admin
from django.urls import path, include, re_path
from core import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', include('accounts.urls')),
    path('', include('dashboard.urls')),
    path('', include('candidate.urls')),
    path('', include('price_plan.urls')),
    # re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
