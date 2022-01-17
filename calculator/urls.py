from django.urls import path
from . import views #the . imports views from the blog folder

app_name = 'calculator'

urlpatterns = [
    path('', views.calculator, name="calculator"),
]
