from django.urls import path
from . import views

urlpatterns = [
    path('job_post/', views.job_post, name='job_post'),
    path('posted_job/', views.posted_job, name='posted_job'),
    path('applied_job/', views.applied_job, name='applied_job'),
    path('delete_applied_job/<int:id>', views.delete_candidate_apply, name='delete_applied_job'),
    path('update_post/<int:pk>', views.UpdateJob.as_view(), name='update_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
]