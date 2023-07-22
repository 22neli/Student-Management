# Importing necessary modules from Django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Importing the Student model and StudentForm from the current app's models.py and forms.py files, respectively
from .models import Student
from .forms import StudentForm


# View for the index page
def index(request):
  # Fetching all student objects from the database and pass them to the 'students/index.html' template
  return render(request, 'students/index.html', {
    'students': Student.objects.all()
  })

# View for viewing a specific student's details
def view_student(request, id):
  # Redirecting the user to the index page
  return HttpResponseRedirect(reverse('index'))

# View for adding a new student
def add(request):
  if request.method == 'POST':
    # If the request method is POST, process the form data
    form = StudentForm(request.POST)
    if form.is_valid():
      # If the form data is valid, extract cleaned data from the form
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      new_gpa = form.cleaned_data['gpa']

      # Creating a new Student instance with the extracted data and saving it to the database
      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
        gpa=new_gpa
      )
      new_student.save()

      # Rendering the 'students/add.html' template with an empty form and a success flag set to True
      return render(request, 'students/add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    # If the request method is not POST, render the 'students/add.html' template with an empty form
    form = StudentForm()
  return render(request, 'students/add.html', {
    'form': StudentForm()
  })

# View for editing an existing student's details
def edit(request, id):
  if request.method == 'POST':
    # If the request method is POST, process the form data
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      #If the form data is valid, save the changes to the existing student record
      form.save()
       # Rendering the 'students/edit.html' template with the form and a success flag set to True
      return render(request, 'students/edit.html', {
        'form': form,
        'success': True
      })
  else:
    # If the request method is not POST, fetch the existing student object and render the 'students/edit.html' template with the form
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'students/edit.html', {
    'form': form
  })

# View for deleting an existing student
def delete(request, id):
  if request.method == 'POST':
    # If the request method is POST, delete the student record from the database
    student = Student.objects.get(pk=id)
    student.delete()
    # After deleting, redirecting the user to the index page
  return HttpResponseRedirect(reverse('index'))
  

     