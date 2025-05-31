from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from .models import Job, Application
from .forms import JobForm, ApplicationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.urls import reverse

# def home(request):
#     return HttpResponse("Welcome to the Job Portal")



# @login_required
# def home(request):
#     return render(request, 'jobs/home.html')
@login_required
def home(request):
    role = request.user.profile.role
    return render(request, 'jobs/home.html', {'role': role})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            user.profile.role = role
            user.profile.save()
            login(request, user)
            return redirect('/?registered=true')
    else:
        form = UserRegisterForm()
    return render(request, 'jobs/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            role = user.profile.role
            if role == 'employer':
                return redirect('/employer/jobs/?login=success')
            else:
                return redirect('/jobs/?login=success')
    else:
        form = AuthenticationForm()
    return render(request, 'jobs/login.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'jobs/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/?logout=true')




@login_required
def employer_jobs(request):
    if request.user.profile.role != 'employer':
        return redirect('home')
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'jobs/employer_jobs.html', {'jobs': jobs})


@login_required
def add_job(request):
    if request.user.profile.role != 'employer':
        return redirect('home')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            job.save()
            return redirect('/employer/jobs/?created=true')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    form = JobForm(request.POST or None, instance=job)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('employer_jobs')
    return render(request, 'jobs/edit_job.html', {'form': form})


@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('employer_jobs')
    return render(request, 'jobs/delete_job.html', {'job': job})


# @login_required
# def job_list(request):
#     if request.user.profile.role != 'candidate':
#         return redirect('home')

#     query = request.GET.get('q')
#     jobs = Job.objects.all()
#     if query:
#         jobs = jobs.filter(Q(title__icontains=query) | Q(location__icontains=query))

#     return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_list(request):
    if request.user.profile.role != 'candidate':
        return redirect('home')

    jobs = Job.objects.all()
    query = request.GET.get('q')
    location = request.GET.get('location')

    if query:
        jobs = jobs.filter(Q(title__icontains=query) | Q(description__icontains=query))

    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, 'jobs/job_list.html', {'jobs': jobs})



@login_required
def apply_job(request, job_id):
    if request.user.profile.role != 'candidate':
        return redirect('home')

    job = get_object_or_404(Job, id=job_id)
    already_applied = Application.objects.filter(job=job, candidate=request.user).exists()
    if already_applied:
        return render(request, 'jobs/already_applied.html', {'job': job})

    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.candidate = request.user
            application.save()
            # return redirect('job_list')
            return redirect(reverse('apply_job', args=[job_id]) + '?submitted=true')
    else:
        form = ApplicationForm()
    return render(request, 'jobs/apply_form.html', {'form': form, 'job': job})


@login_required
def view_applicants(request, job_id):
    if request.user.profile.role != 'employer':
        return redirect('home')

    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applications = Application.objects.filter(job=job)
    return render(request, 'jobs/view_applicants.html', {
        'job': job,
        'applications': applications
    })

