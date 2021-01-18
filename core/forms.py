from django import forms
from django.contrib.auth.models import User
from core.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)
    
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)