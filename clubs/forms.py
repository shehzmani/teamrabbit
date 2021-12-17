from django import forms
from .models import User

class SignUpForm(forms.ModelForm):
     class Meta:
        model = User
        fields = ['first name', 'last name', 'username','email', 'bio', 'personal statement']
     new_password = forms.CharField(label='password',widget=forms.PasswordInput())
     password_confirmation =forms.CharField(label='password confirmation',widget=forms.PasswordInput())
