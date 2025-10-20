from django.contrib import admin
from .models import Course, Semester
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('course', 'semester_number')
    list_filter = ('course',)
    search_fields = ('course__name', 'semester_number')