from django.contrib import admin
from django.urls import path, include
# from employee_information.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls, name="admin-site"),
    # path('', landing_page, name='landing-page'),  # Landing page as the default route
    path('', include('employee_information.urls')),
]
