from django import forms
from app.models import Students, Course, Project

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class ProjectForm(forms.ModelForm): 
    class Meta: 
        model = Project 
        fields = ('topic', 'languages_used', 'duration') 
        widgets = { 
        'topic': forms.TextInput(attrs={'class': 'form-control'}), 
        'languages_used': forms.TextInput(attrs={'class': 'form-control'}), 
        'duration': forms.TextInput(attrs={'class': 'form-control'}), 
        }