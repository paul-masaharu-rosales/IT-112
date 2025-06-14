from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['firstName', 'lastName', 'grade', 'gpa', 'classes']
    list_filter = ['firstName', 'lastName', 'grade', 'gpa', 'classes']
    list_display = ['firstName', 'grade', 'gpa']


admin.site.register(Student, StudentAdmin)