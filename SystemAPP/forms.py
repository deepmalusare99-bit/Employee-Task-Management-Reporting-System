# forms.py
from .models import Task, Employee
from .models import Task
from .models import Contact
from .models import Department
from django import forms
from .models import Employee

from django import forms
from .models import Task, Contact, Department, Employee
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'mobile', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter mobile number'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }


# forms.py


class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter task title'})
    )

    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter task description'})
    )

    assigned_to = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label="Select User"
    )

    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'assigned_to',
            'status',
            'due_date',
        ]


# forms.py


class EmployeeSignUpForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # Add additional form fields here as needed
