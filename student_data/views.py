from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Course, Semester
# Create your views here.
@login_required
def student_dashboard(request):
    return render(request, 'student_data/student_dashboard.html')


@login_required
def student_profile(request):
    if request.method == 'POST':
        user = request.user
        course_id = request.POST.get('course')
        semester_id = request.POST.get('semester')

        # Fetch the Course and Semester instances
        try:
            course = Course.objects.get(id=course_id) if course_id else None
            semester = Semester.objects.get(id=semester_id) if semester_id else None
        except (Course.DoesNotExist, Semester.DoesNotExist):
            return JsonResponse({'error': 'Invalid course or semester ID'}, status=400)

        # Assign the instances to the user
        user.course = course
        user.semester = semester
        user.save()

        return redirect('student_profile')

    return render(request, 'student_data/profile.html')

@login_required
def get_student_profile(request):
    if request.method == 'GET':
        user = request.user
        profile_data = {
            'id': user.id,
            'course': {
                'id': user.course.id,
                'name': user.course.name
            } if user.course else None,
            'semester': {
                'id': user.semester.id,
                'semester_number': user.semester.semester_number
            } if user.semester else None
        }
        return JsonResponse(profile_data)

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_courses(request):
    courses = Course.objects.all().values('id', 'name')
    return JsonResponse(list(courses), safe=False)

def get_semesters(request, course_id):
    semesters = Semester.objects.filter(course_id=course_id).values('id', 'semester_number')
    return JsonResponse(list(semesters), safe=False)