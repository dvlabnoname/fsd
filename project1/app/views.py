from django.shortcuts import render, redirect
import datetime
from .models import Students, Course, Project
from .forms import StudentForm, CourseForm, ProjectForm
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
import csv
from reportlab.pdfgen import canvas

def date_time(request, t):
    c = datetime.datetime.now()
    t = int(t)
    context = {
        'current':c,
        'ahead': f'{t} hrs ahead time is {c+datetime.timedelta(hours=t)}',
        'behind': f'{t} hrs behind time is {c-datetime.timedelta(hours=t)}'
    }

    return render(request, 'datetime.html', context)



def fruit_student(request):
    std = {'wdefrv', 'defrvf'}
    frt = {'Apple', 'Orange', 'Bananna', 'Grapes'}
    context = {
        'fruits':frt,
        'students':std
    }

    return render(request, 'fruit_std/list.html', context)




def home_page(request):
    return render(request, 'layout/home.html')
def contact(request):
    return render(request, 'layout/contact.html')
def about(request):
    return render(request, 'layout/about.html')





def student_list(request):
    courses = Course.objects.all()
    cid = request.POST.get('course')
    students = Students.objects.all()
    if(request.method=='POST'):
        if(cid!='All'):
            course = Course.objects.get(id=cid)
            students = course.enrollment.all()
    return render(request, 'stdreg/studentlist.html', {'students':students, 'course':courses})

def course_list(request):
    course = Course.objects.all()
    return render(request, 'stdreg/courselist.html', {'course':course})

def student_reg(request):
    if(request.method=='POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('studentlist')
        
    form = StudentForm()
    return render(request, 'stdreg/regstd.html', {'form':form})

def course_reg(request):
    if(request.method=='POST'):
        form = CourseForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('courselist')
    form = CourseForm()
    return render(request, 'stdreg/regcrs.html', {'form':form})

def enrollment(request):
    students = Students.objects.all().values()
    courses = Course.objects.all().values()
    if(request.method=='POST'):
        course = Course.objects.get(id=request.POST.get('course'))
        student = Students.objects.get(id=request.POST.get('student'))
        course.enrollment.add(student)
    return render(request, 'stdreg/enrollment.html', {'students':students, 'course':courses})
    





def register_project(request):
    form = ProjectForm() 
    if request.method == 'POST': 
        form = ProjectForm(request.POST) 
        if form.is_valid(): 
            form.save() 
            return redirect('index')  
    return render(request, 'projectForm/project_register.html', {'form': form}) 

def project_details(request, id):
    project = Project.objects.get(id=id)
    return render(request, 'projectForm/project_student.html', {'project':project})

def index(request): 
    courses = Course.objects.all() 
    projects = Project.objects.all() 
    return render(request, 'projectForm/index.html', { 
    'projects': projects, 
    })




class StudentListView(ListView): 
    model = Students
    template_name = 'generic/stu_list.html' 
    context_object_name = 'students'


class StudentDetailView(DetailView): 
    model = Students
    template_name = 'generic/student_detail.html' 
    context_object_name = 'student'



def csv_file(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=file.csv'
    writer = csv.writer(response)
    writer.writerow(['Student name', 'USN'])
    students = Students.objects.all()
    for student in students:
        writer.writerow([student.name, student.usn])
    
    return response

def pdf_file(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=file.pdf'
    p = canvas.Canvas(response)
    y = 800
    p.drawString(100, y, 'Student name   USN')
    y = y-50
    students = Students.objects.all()
    for student in students:
        p.drawString(100, y, f'{student.name}, {student.usn}')
        y = y-50
    p.showPage()
    p.save()
    return response
    