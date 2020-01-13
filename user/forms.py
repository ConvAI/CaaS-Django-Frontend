from django import forms
from user.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    c_password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','c_password','email')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('c_name','c_desc','c_type','c_url','c_logo')