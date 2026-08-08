from django.db import models

# Create your models here.
class UserProfile(models.Model):
    firstName=models.CharField(max_length=100)
    lastName=models.CharField(max_length=100)
    # Date_of_joining=models.CharField(max_length=100)
    Email=models.EmailField(unique=True)
    courses=models.CharField(default="python")
    