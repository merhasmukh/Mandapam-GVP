"""
URL configuration for attendance_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from attendance_sys import views as attendance_views
from django.urls import path
from allauth.socialaccount.providers.google.views import OAuth2LoginView
from student_data import views as student_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth URLs
    path('attendance/', include('take_attendance.urls')),
    path('', attendance_views.home, name='home'),
    path('accounts/google/login/', OAuth2LoginView.as_view(), name='socialaccount_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Add this line
    path('student_dashboard/', include('student_data.urls')),  # Add this line
    path('api/courses/', student_views.get_courses, name='get_courses'),
    path('api/semesters/<int:course_id>/', student_views.get_semesters, name='get_semesters'),

]
