from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_dashboard, name='student_dashboard'),
    path('student_profile/', views.student_profile, name='student_profile'),
    path('get_student_profile/', views.get_student_profile, name='get_student_profile'),


]

