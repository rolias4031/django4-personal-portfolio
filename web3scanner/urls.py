from django.urls import path
from . import views #the . imports views from the web3scanner folder

app_name = 'web3scanner'

urlpatterns = [
    path('', views.scanner, name="web3scanner"),
]
