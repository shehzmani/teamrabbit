from django import forms
from django.core.exceptions import ValidationError
from . import models

class ApplicantForm(forms.Form):
    name = forms.CharField(label="Name", error_messages={"required": "Required!"})
    email = forms.CharField(label="E-mail", error_messages={"required": "Required!"})
    public_bio = forms.CharField(label="Public Bio", error_messages={"required": "Required!"})
    chess_experience = forms.CharField(label="Chess Experience", error_messages={"required": "Required!"})
    personal_statement = forms.CharField(label="Personal Statement", error_messages={"required": "Required!"})
    aim_club = forms.CharField(label="Aim Club", error_messages={"required": "Required!"})
    