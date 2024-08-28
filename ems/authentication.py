# ems/authentication.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from employee_information.models import Employees

class EmployeeBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Employees.objects.get(email=username)
            if user.code == password:
                return user
        except Employees.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employees.objects.get(pk=user_id)
        except Employees.DoesNotExist:
            return None
