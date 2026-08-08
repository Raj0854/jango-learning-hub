from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("batches/", views.batches, name="batches"),
    path("courses/", views.courses, name="courses"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("profiles/", views.profiles, name="profiles"),
]
