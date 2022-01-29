"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'), name="blog"),
    path('dictionary/', include('dictionary.urls'), name="dictionary"),
    path('passwordgenerator/', include('passwordgenerator.urls'), name='passwordgenerator'),
    path('calculator/', include('calculator.urls'), name='calculator'),
    path('web3scanner/', include('web3scanner.urls'), name='web3scanner'),

]

"""
we added this to allow access to our MEDIA_ROOT setting. this is the second half of that process of creating and specifying where we want all our media to be stored.
"""

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
