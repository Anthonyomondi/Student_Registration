# Student_Registration

## Introduction

>Python Django project for implementing CRUD(Create, Retrieve, Update, Delete)  operations

## Technlogies

 Django==3.2,
 django-crispy-forms==1.11.2,
 bootstrap4,
 Database - PostgreSQL


## Code Samples

```
class Course(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    student_id = models.CharField(max_length=5)
    mobile = models.CharField(max_length=13)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
```

```
def student_form(request,id=0):
    if request.method == 'GET':
        if id==0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance = student)
        return render(request,"student_reg/student_form.html",{'form':form})
    else:
       
```

## Installation

>Clone repository to your local system

>Activate virtual environment:

     Run local_dir\stu_env\scripts\activate

>Access rendered site in localhost
    
    http://localhost:8000/student/
    
## Useful Links:

    https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/
