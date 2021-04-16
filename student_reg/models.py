from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    student_id = models.CharField(max_length=5)
    mobile = models.CharField(max_length=13)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
