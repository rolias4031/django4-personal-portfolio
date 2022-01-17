from django.shortcuts import render
from .models import Project

# Create your views here.
"""
- this file is where we "grab" all the project objects. we put the objects into a variable "projects" so that we can configure and display them on the home.html page.
- we put the projects object list into a dictionary into the return statement so that we can loop through them using the templating language on home.html
"""

def home(request):
    projects = Project.objects.all() #grabs all the objects from the database that use the Project class

    return render(request, 'portfolio/home.html', {'projects': projects})
