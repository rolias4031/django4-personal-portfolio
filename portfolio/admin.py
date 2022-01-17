from django.contrib import admin
from .models import Project

"""
Register your models here.
- this file is where you link your models to your admin interface after you makemigrations and migrate.
- .models gets the models.py file in this folder and gets the Project class that we created with all the fields.
"""
admin.site.register(Project)
