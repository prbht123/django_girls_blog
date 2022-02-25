from django import forms
from .models import UserProfile



class PostForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('name', 'about_me','address','city','state','country','email','phone_number')