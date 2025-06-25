from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import  User 
from .models import Profile

class userRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    mobile = forms.CharField(max_length=15, required=False, help_text='Optional. Enter your mobile number.')

    class Meta:
        model = User
        fields = ('username', 'email', 'mobile','password1', 'password2')

class userUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email' )

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image',)

    