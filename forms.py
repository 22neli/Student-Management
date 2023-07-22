# Importing necessary modules from Django
from django import forms
# Importing the Student model from the current app's models.py file
from .models import Student

# Creating a form class that is based on the Student model
class StudentForm(forms.ModelForm):
     # Defining the form's metadata using the 'Meta' class
    class Meta:
        # Setting the model that the form is based on
        model = Student
        # Defining the fields that should be included in the form
        fields= ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
        # Defining custom labels for the form fields
        labels = {
            'student_number': 'Student Number', 
            'first_name': 'First Name', 
            'last_name': 'Last Name', 
            'email': 'Email', 
            'field_of_study': 'Field of Study', 
            'gpa': 'GPA'
        }   
        # Defining widgets that will be used to render the form fields with specific attributes
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
            'first_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'last_name': forms.TextInput(attrs={'class': 'form-control'}), 
            'email': forms.EmailInput(attrs={'class': 'form-control'}), 
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}), 
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}), 
        }
        