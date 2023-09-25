from django.urls import path
from . import views

urlpatterns = [
    path('job_detail/<int:id>', views.job_detail, name='job_detail'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/<int:pk>', views.UpdateProfile.as_view(), name='update_profile'),
    path('apply_job/<int:id>', views.apply_job, name='apply_job'),
]
