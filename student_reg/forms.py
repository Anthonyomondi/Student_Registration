from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'fullname': 'Full Name',
            'student_id': 'STUDENT ID',
        }
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['course'].empty_label = "Select"
        self.fields['student_id'].required = False #removes required validation for stated field