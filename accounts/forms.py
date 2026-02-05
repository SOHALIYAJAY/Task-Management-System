from django import forms
from django.contrib.auth import get_user_model
from accounts.models import CustomUser

User=get_user_model()

class UserRegistrationForm(forms.ModelForm):
    
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=['name','email','phone','password1','password2']


        def clean(self):
            clean_data=super().clean()
            p1=clean_data.get('password1')
            p2=clean_data.get('password2')

            if p1 and p2 and p1!=p2:
                return forms.ValidationError('Enter the Valid Fields')
            return clean_data