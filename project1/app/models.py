from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    sem = models.IntegerField()
    usn = models.CharField(max_length=10)

    def __str__(self):
        return f'name:{self.name}, sem:{self.sem}, usn:{self.usn}'
    
class Course(models.Model):
    course = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    credits = models.IntegerField()

    enrollment = models.ManyToManyField(Students, blank=True)

    def __str_(self):
        return f'Course = {self.course}, Code = {self.course_code}, Credits = {self.credits}'




class Project(models.Model): 
    topic = models.CharField(max_length=100, default='') # Added default value for topic 
    languages_used = models.CharField(max_length=100, default='') 
    duration = models.IntegerField(default=0) 
    def  str (self): 
        return self.topic 