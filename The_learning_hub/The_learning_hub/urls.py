"""
URL configuration for The_learning_hub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from info import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('batches/', views.batches, name='batches'),
    path('courses/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('free_tutorials/', views.free_tutorials, name='free_tutorials'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('forget_password/', views.forget_password, name='forget_password'),
]
