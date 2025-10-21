from django.contrib.auth.models import AbstractUser
from django.db import models
from student_data.models import Course, Semester
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('cr', 'Class Representative'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, blank=True, null=True)
    @property
    def is_cr(self):
        return self.role == 'cr'


   
       
