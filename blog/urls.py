from django.urls import path
from . import views #the . imports views from the blog folder

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name="all_blogs"),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('survivordao/', views.survivordao_display, name='survivordao_display')
]
