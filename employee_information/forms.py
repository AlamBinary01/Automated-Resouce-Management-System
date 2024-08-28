# forms.py

from django import forms
from .models import Student,MaintenanceTask
from django.contrib.auth.hashers import make_password

class MaintenanceTaskForm(forms.ModelForm):
    class Meta:
        model = MaintenanceTask
        fields = ['equipment', 'task_name', 'scheduled_date', 'completed']
        

class EmployeeLoginForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    code = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Code'}))

class StudentSignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender', 
            'contact_number', 'address', 'email', 'username', 'password'
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password and Confirm Password do not match.")
        return cleaned_data

    def save(self, commit=True):
        student = super().save(commit=False)
        student.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            student.save()
        return student
    
class StudentLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)