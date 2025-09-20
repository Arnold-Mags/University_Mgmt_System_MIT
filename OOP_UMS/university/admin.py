from django.contrib import admin
from .models import Student, Professor, Course, Department
from django.contrib.contenttypes.admin import GenericTabularInline

# Register your models here.

admin.site.site_header = "System Admin"
admin.site.site_title = "Administrator Area"
admin.site.index_title = "Welcome to the Administrator Panel!"

CourseStudent = Course.students.through
CourseStudent._meta.verbose_name = "Student Course"
CourseStudent._meta.verbose_name_plural = "Student Courses"

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'department', 'salary')
    search_fields = ('name', 'employee_id', 'dept_name')
    list_filter = ('department',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id', 'major', 'gpa', 'enrollment_date')
    search_fields = ('name', 'student_id', 'major')
    list_filter = ('major', 'enrollment_date')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_name', 'budget')
    search_fields = ('dept_name',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'title', 'credits', 'professor')
    search_fields = ('course_code', 'title', 'professor__name')
    list_filter = ('credits', 'professor__department')

class CourseStudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course')
    search_fields = ('course__course_code', 'course__title', 'student__name', 'student__student_id')
    list_filter = ('course', 'student')

admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(CourseStudent, CourseStudentAdmin)

