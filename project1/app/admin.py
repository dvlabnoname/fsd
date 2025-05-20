from django.contrib import admin
from app.models import Students, Course
class StudentAdmin(admin.ModelAdmin):
    fields = ('name', 'usn', 'sem')
    list_display = ('name', 'usn')
    list_filter = ('name',)

class CourseAdmin(admin.ModelAdmin):
    fields = ('course', 'course_code', 'credits')
    list_display = ('course', 'course_code')

admin.site.register(Students, StudentAdmin)
admin.site.register(Course, CourseAdmin)