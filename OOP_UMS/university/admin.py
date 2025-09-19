from django.contrib import admin
from .models import Student, Professor, Course, Department
from django.contrib.contenttypes.admin import GenericTabularInline


admin.site.site_header = "System Admin"
admin.site.site_title = "Administrator Area"
admin.site.index_title = "Welcome to the Administrator Panel!"

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Department)

# Register your models here.

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'department', 'salary')
    search_fields = ('name', 'employee_id', 'department__dept_name')
    list_filter = ('department',)
    inlines = [CourseInline]

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'major', 'gpa', 'enrollment_date')
    search_fields = ('name', 'student_id', 'major')
    list_filter = ('major', 'enrollment_date')
    inlines = [CourseInline]


