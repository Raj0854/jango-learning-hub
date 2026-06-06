from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return  render(request, 'index.html')

def batches(request):
    return render(request, 'batches.html')

def courses(request):
    return render(request, 'courses.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
def free_tutorials(request):
    return render(request, 'free_tutorials.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request, 'register.html')