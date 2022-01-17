from django.urls import path
from . import views #the . imports views from the blog folder

app_name = 'passwordgenerator'

urlpatterns = [
    path('', views.generator, name="passwordgenerator"),
]
