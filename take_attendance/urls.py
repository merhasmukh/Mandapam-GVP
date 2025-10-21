from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_location_view, name='check_location_api'),
    path('get-location/', views.get_location, name='get_location'),
    path('api/check-location/', views.check_location_view, name='check_location_api'),
    path('mark-attendance/', views.mark_attendance, name='mark_attendance'),
]

