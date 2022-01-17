from django.urls import path
from . import views #the . imports views from the blog folder

app_name = 'dictionary'

urlpatterns = [
    path('', views.dictionary, name="dictionary"),
]
