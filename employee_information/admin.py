from django.contrib import admin
from employee_information.models import Department, Position, Employees,Student,Course,Student_bio,Announcement,MaintenanceTask,Equipment,Attendance

# Register your models here.
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employees)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Student_bio)
admin.site.register(Announcement)
admin.site.register(MaintenanceTask)
admin.site.register(Equipment)
admin.site.register(Attendance)

