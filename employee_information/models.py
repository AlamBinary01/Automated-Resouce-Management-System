from datetime import datetime
from django.db import models
from django.utils import timezone

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)  # Store hashed password
    courses = models.ManyToManyField('Course', related_name='students')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Department(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.TextField() 
    description = models.TextField() 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
    position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' + (self.middlename or '') + ' ' + self.lastname

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    


class Student_bio(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]


    student_bio_id = models.CharField(max_length=100, blank=True)  # Unique student ID
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)  # Date of Birth
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)  # Assuming course as position here
    date_enrolled = models.DateField()  # Enrollment Date
    status = models.IntegerField()  # 1 for active, 0 for inactive
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.middle_name or ''} {self.last_name}"
    


class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


class Equipment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class MaintenanceTask(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=200)
    scheduled_date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_name} for {self.equipment.name}"
    


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    ]

    student = models.ForeignKey(Student_bio, on_delete=models.CASCADE)  # Link to the Student_bio model
    date = models.DateField(default=timezone.now)  # Attendance date
    status = models.CharField(max_length=7, choices=STATUS_CHOICES, default='Absent')  # Attendance status
    remarks = models.TextField(blank=True, null=True)  # Optional remarks field
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student', 'date')  # Ensure each student has one attendance record per date

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
