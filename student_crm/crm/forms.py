from django import forms

from .models import Course, Enrollment, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'phone', 'address']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'duration', 'description']


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course']
