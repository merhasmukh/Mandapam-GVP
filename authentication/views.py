from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User

def google_sign_in_callback(request):
    # Example callback after Google sign-in
    user = request.user
    if not user.role:  # Assign default role if not set
        user.role = 'student'
        user.save()
    return redirect('student_dashboard')

from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    if request.user.role == 'student':
        return render(request, 'student_data/student_dashboard.html')
    elif request.user.role == 'cr':
        return render(request, 'student_data/cr_dashboard.html')
    else:
        return render(request, 'student_data/access_denied.html')
