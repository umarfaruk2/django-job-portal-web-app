from django.urls import path
from . import views

urlpatterns = [
    path('job_detail/<int:id>', views.job_detail, name='job_detail')
]
