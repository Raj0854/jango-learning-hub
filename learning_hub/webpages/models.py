from django.db import models
from django.utils import timezone
# Create your models here.
class UserProfile(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    contactNumber=models.CharField(max_length=15,null=True)
    Date_of_Enquiry=models.DateField(default=timezone.localdate)
    Email=models.EmailField(unique=True)
    courses=models.CharField(null=True)
    