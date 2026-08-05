from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def batches(request):
    return render(request,"batches.html")
def courses(request):
    return render(request,"courses.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")