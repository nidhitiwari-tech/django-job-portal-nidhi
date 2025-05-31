from django.contrib import admin
from .models import Profile, Job, Application

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role']
    search_fields = ['user__username', 'role']

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'salary', 'posted_by', 'posted_date', 'expiry_date']
    list_filter = ['location', 'posted_date']
    search_fields = ['title', 'description', 'location']

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['job', 'candidate', 'applied_on']
    search_fields = ['job__title', 'candidate__username']
