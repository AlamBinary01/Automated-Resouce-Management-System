from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from .views import export_departments_to_excel

urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"), name="redirect-admin"),
    path('', views.home, name="home-page"),
    path('login', auth_views.LoginView.as_view(template_name='employee_information/login.html', redirect_authenticated_user=True), name="login"),
    path('userlogin', views.login_user, name="login-user"),
    path('logout', views.logoutuser, name="logout"),
   
    path('about', views.about, name="about-page"),
    #department
    path('departments', views.departments, name="department-page"),
    path('manage_departments', views.manage_departments, name="manage_departments-page"),
    path('save_department', views.save_department, name="save-department-page"),
    path('delete_department', views.delete_department, name="delete-department"),
    path('export-departments-excel/', export_departments_to_excel, name='export-departments-excel'),
    #courses
     path('courses', views.courses, name="course-page"),
    path('manage_courses', views.manage_courses, name="manage_courses-page"),
    path('save_course', views.save_course, name="save-course-page"),
    path('delete_course', views.delete_course, name="delete-course"),
    path('export_courses/', views.export_courses_to_excel, name='export_courses'),
    #positions
    path('positions', views.positions, name="position-page"),
    path('manage_positions', views.manage_positions, name="manage_positions-page"),
    path('save_position', views.save_position, name="save-position-page"),
    path('delete_position', views.delete_position, name="delete-position"),
     path('export_positions/', views.export_positions_to_excel, name='export_positions'),
    #employee
    path('employees', views.employees, name="employee-page"),
    path('manage_employees', views.manage_employees, name="manage_employees-page"),
    path('save_employee', views.save_employee, name="save-employee-page"),
    path('delete_employee', views.delete_employee, name="delete-employee"),
    path('view_employee', views.view_employee, name="view-employee-page"),
    path('charts/', views.charts_page, name='charts-page'), 
    path('export_employees/', views.export_employees_to_excel, name='export_employees'),

    #students-bio
    path('students/', views.students, name="student-page"),
    path('manage_students/', views.manage_students, name="manage_students-page"),
    path('save_student/', views.save_student, name="save-student-page"),
    path('delete_student/', views.delete_student, name="delete-student"),
    path('view_student/', views.view_student, name="view-student-page"),
#user
    # path('signup-user/', views.signup, name='signup'),
    # path('login-user/', views.loginUser, name='login-user'),
    # path('home-user/', views.homePage, name='home-page'),

    path('announcements/', views.announcements, name='announcements-list'),
    path('manage_announcement/', views.manage_announcement, name='manage-announcement'),
    path('save_announcement/', views.save_announcement, name='save-announcement'),
    path('delete_announcement/', views.delete_announcement, name='delete-announcement'),

    #maintainence 
    path('maintenance_tasks', views.maintenance_tasks, name="maintenance-tasks-page"),
    path('manage_maintenance_task', views.manage_maintenance_tasks, name="manage-maintenance-task-page"),
    path('save_maintenance_task', views.save_maintenance_task, name="save-maintenance-task-page"),
    path('delete_maintenance_task', views.delete_maintenance_task, name="delete-maintenance-task"),
    # path('export-maintenance-tasks-excel/', view, name='export-maintenance-tasks-excel'),

    path('attendance/', views.attendance_list, name='attendance-list'),
    path('manage_attendance/', views.manage_attendance, name='manage-attendance'),
    path('save_attendance/', views.save_attendance, name='save-attendance'),
    path('delete_attendance/', views.delete_attendance, name='delete-attendance'),
#############################################################

    path('login-emp/', views.login_emp, name='login_emp'),
    path('home-emp/',views.home_emp, name='home-emp'),
    path('logout-emp/', views.logout_emp, name='logout-emp'),

################################################################

    path('news/', views.news_list, name='news-list'),


###############################<- STUDENT MODULE -> ##################################

    path('student-signup/', views.student_signup, name='student-signup'),
    path('student-login/', views.student_login, name='student-login'),
    path('home/', views.home_page, name='home-page-student'),  # Ensure this is correct
    path('courses/', views.course_list, name='course_list'),
    path('announcements-list/',views.announcement_list, name='announcement_list'),
    path('educational-news/', views.eudcation_news_list, name='educational-news-list'),
    path('department-list',views.department_list,name='student-department-list'),
    path('logout-student', views.student_logout, name="student-logout"),

    
]