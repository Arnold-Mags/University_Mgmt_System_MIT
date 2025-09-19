from django.db import models

# Abstract Base Class
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    phone = models.CharField(max_length=15)

    class Meta:
        abstract = True

    def get_contact_info(self):
        return f"{self.name} | {self.email} | {self.phone}"


# Student extends Person
class Student(Person):
    student_id = models.CharField(max_length=20, unique=True)
    major = models.CharField(max_length=100)
    gpa = models.FloatField()
    enrollment_date = models.DateField()

    def enroll(self, course):
        self.courses.add(course)

    def __str__(self):
        return f"{self.name} ({self.student_id})"


# Department model
class Department(models.Model):
    dept_name = models.CharField(max_length=100, unique=True)
    budget = models.FloatField()

    def add_professor(self, professor):
        self.professors.add(professor)

    def __str__(self):
        return self.dept_name


# Professor extends Person
class Professor(Person):
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="professors")
    salary = models.FloatField()

    def add_course(self, course):
        self.courses_taught.add(course)

    def __str__(self):
        return f"Prof. {self.name} ({self.employee_id})"


# Course model
class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    credits = models.IntegerField()
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True, related_name="courses_taught")
    students = models.ManyToManyField(Student, related_name="courses")

    def add_student(self, student):
        self.students.add(student)

    def __str__(self):
        return f"{self.course_code} - {self.title}"