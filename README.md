Job Portal - Django POC Project

This is a Django-based Job Portal application built as part of a POC assessment.

Objective:

Build a system where:
- Employers can post jobs and view applicants.
- Candidates can register, browse jobs, and apply.
- Admin can manage all jobs, users, and applications via Django Admin.

 Tech Stack:

Backend: Django
-Database: PostgreSQL
-Auth: Django’s built-in authentication
- UI: Django Templates, Bootstrap 5, SweetAlert2
- Bonus: Role-based login redirects, search & filter, styled forms


 Setup Instructions:

1. Clone the repo & install requirements
git clone https://github.com/nidhitiwari-tech/django-job-portal-nidhi.git
cd job_portal
pip install -r requirements.txt

2. PostgreSQL Setup
Update `job_portal/settings.py` with your PostgreSQL credentials:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'job_portal_db',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

Create the database `job_portal_db` in PostgreSQL manually.

3. Run Migrations & Start Server
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

User Roles

- Admin: Can access Django Admin panel at `/admin/`
- Employer:
  - Can post/edit/delete jobs
  - Can view applicants
- Candidate:
  - Can view/apply to jobs
  - Can search by title/location


Features

- Full user authentication
- Role-based dashboard
- Job posting + application
- Resume upload
- SweetAlert feedback (registration, login, apply)
- Bootstrap UI with cards, navbar, etc.


Made by Nidhi Tiwari
