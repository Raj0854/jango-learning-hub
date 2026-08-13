from django  import forms
from .models import UserProfile
class Enquiryform(forms.ModelForm):
    class Meta:
        model =UserProfile
        fields = {'firstName','lastName','contactNumber','Email','courses'}