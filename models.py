from django.db import models

# Defining a Django model called 'Student'
class Student(models.Model):
    # Defining a field to store the student number as a positive integer
    student_number = models.PositiveIntegerField()
    # Defining a field to store the first name as a character field with a maximum length of 50 characters
    first_name = models.CharField(max_length=50)
    # Defining a field to store the last name as a character field with a maximum length of 50 characters
    last_name = models.CharField(max_length=50)
    # Defining a field to store the email address as an EmailField with a maximum length of 100 characters
    email = models.EmailField(max_length=100)
    # Defining a field to store the field of study as a character field with a maximum length of 50 characters
    field_of_study = models.CharField(max_length=50)
    # Defining a field to store the GPA (Grade Point Average) as a floating-point number
    gpa = models.FloatField()


    # Defining a string representation for the model instance
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name}'
    