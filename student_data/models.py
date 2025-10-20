from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Semester(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester_number = models.IntegerField()

    def __str__(self):
        return f"{self.course.name} - Semester {self.semester_number}"     