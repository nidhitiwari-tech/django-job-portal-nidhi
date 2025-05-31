from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('employer/jobs/', views.employer_jobs, name='employer_jobs'),
    path('employer/jobs/add/', views.add_job, name='add_job'),
    path('employer/jobs/edit/<int:job_id>/', views.edit_job, name='edit_job'),
    path('employer/jobs/delete/<int:job_id>/', views.delete_job, name='delete_job'),
    path('jobs/', views.job_list, name='job_list'),
    path('jobs/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('employer/jobs/<int:job_id>/applicants/', views.view_applicants, name='view_applicants'),
]

