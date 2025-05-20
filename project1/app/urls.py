from django.urls import path
from app.views import (date_time, fruit_student, home_page, about, project_details, contact, student_list, course_list,course_reg, student_reg, enrollment, register_project, index, StudentDetailView, StudentListView, csv_file, pdf_file)
urlpatterns =[
    path('list', fruit_student, name='list'),


    path('datetime/<str:t>', date_time, name='datetime'),


    path('home', home_page, name='main'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),


    path('studentlist', student_list, name='studentlist'),
    path('courselist', course_list, name='courselist'),
    path('enrollment', enrollment, name='enrollment'),
    path('regstd', student_reg),
    path('regcrs', course_reg),



    path('index', index, name='index'),
    path('project_student/<int:id>', project_details, name='project_student'),
    path('project_register/', register_project, name='project_register'),


    path('stu_list/', StudentListView.as_view(), name='stu_list'), 
    path('student_detail/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),

    path('csv_file', csv_file, name='csv_file'),
    path('pdf_file', pdf_file, name='pdf_file')
]