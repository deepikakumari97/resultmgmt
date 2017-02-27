from django.contrib import admin

# Register your models here.
from .models import *

class ResultsInline(admin.TabularInline):
    model = Result 
    extra = 1

class StudentAdmin(admin.ModelAdmin):
    search_fields = ['name','rollNo']
    list_display = ('name', 'rollNo','branch', 'semester')
    list_filter = ['branch','semester']
    inlines = [ResultsInline]



admin.site.register(Student, StudentAdmin)

class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['title', 'code']
    inlines = [ResultsInline]
    list_display = ('code', 'title','credit')

admin.site.register(Subject, SubjectAdmin)

