from django.urls import path
from . import views

# Defining the URL patterns for the website
urlpatterns = [
     # URL pattern for the index page (homepage)
    # When a user visits the base URL (e.g., 'example.com/'), it will trigger the 'index' view function from the 'views' module
    # The 'name' parameter allows us to reference this URL pattern by its name ('index') in other parts of the code
    path('', views.index, name='index'),
    # URL pattern to view a specific student's details
    # The '<int:id>' part is a URL parameter, allowing us to capture an integer value from the URL and pass it to the 'view_student' view function
    # For example, 'example.com/1' will trigger the 'view_student' view function with id=1
    # The 'name' parameter allows us to reference this URL pattern by its name ('view_student') in other parts of the code
    path('<int:id>', views.view_student, name='view_student'),
    # URL pattern for adding a new student
    # When a user visits 'example.com/add/', it will trigger the 'add' view function from the 'views' module
    # The 'name' parameter allows us to reference this URL pattern by its name ('add') in other parts of the code
    path('add/', views.add, name='add'),
    # URL pattern for editing an existing student's details
    # The '<int:id>/' part is a URL parameter, allowing us to capture an integer value from the URL and pass it to the 'edit' view function
    # For example, 'example.com/edit/1/' will trigger the 'edit' view function with id=1
    # The 'name' parameter allows us to reference this URL pattern by its name ('edit') in other parts of the code
    path('edit/<int:id>/', views.edit, name='edit'),
    # URL pattern for deleting an existing student
    # The '<int:id>/' part is a URL parameter, allowing us to capture an integer value from the URL and pass it to the 'delete' view function
    # For example, 'example.com/delete/1/' will trigger the 'delete' view function with id=1
    # The 'name' parameter allows us to reference this URL pattern by its name ('delete') in other parts of the code
    path('delete/<int:id>/', views.delete, name='delete'),
]