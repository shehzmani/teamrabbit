from django import forms
from.models import User

class SignUpForm(forms.ModelForm):
     class Meta:
        model = User
<<<<<<< HEAD
        fields = ['first name', 'last name', 'username','email', 'bio', 'personal statement']
=======
        fields = ['first name', 'last name', 'username','Email'，'public bio','chess experience level']
    
>>>>>>> 4726a401120f096739d9d1613cbc813cfa352b02
     new_password = forms.CharField(label='password',widget=forms.PasswordInput())
     password_confirmation =forms.CharField(label='password confirmation',widget=forms.PasswordInput())
