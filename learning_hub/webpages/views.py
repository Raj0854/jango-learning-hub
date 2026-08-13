from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile
from .forms import Enquiryform
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
def Enquiry(request):
    profiles =UserProfile.objects.all()
    return render(request,"enquiry.html",{'profiles' :profiles})
def enquiry_form(request):
    if request.method == 'POST':
        form =Enquiryform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=Enquiryform()
    return render(request,"enquiry_form.html",{'form':form})