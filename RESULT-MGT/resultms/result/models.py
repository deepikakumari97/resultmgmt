from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    rollNo = models.CharField(max_length=30, unique=True, blank=True, null=True)
    branch = models.CharField(max_length=30, blank=True, null=True)
    semester = models.IntegerField()

    def __str__(self):
        return self.name
        

class Subject(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30, blank=True, null=True)
    credit = models.IntegerField()

    def __str__(self):
        return self.title

class Result(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject',on_delete=models.CASCADE)
    grade_choices=(
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    grade = models.CharField(max_length=2, choices=grade_choices, default='F')



