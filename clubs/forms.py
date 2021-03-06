from django import forms
from.models import User

class SignUpForm(forms.ModelForm):
     class Meta:
        model = User
        fields = ['first name', 'last name', 'username','email', 'bio', 'personal statement']
        new_password = forms.CharField(label='password',widget=forms.PasswordInput())
        password_confirmation =forms.CharField(label='password confirmation',widget=forms.PasswordInput())

#Create form that will allow the user to enter data to create a new club
class CreateClubForm(forms.Form):
    name = forms.CharField(label="Name")
    location = forms.CharField(label="Location")
    description=forms.CharField(label="Description", widget=forms.Textarea())

    #Will create the form using the data given by the form
    def save(self):
        super().save(commit=False)
        club = Club.objects.create(
            name = self.cleaned_data.get('name'),
            location = self.cleaned_data.get('location'),
            description = self.cleaned_data.get('description'),
        )
