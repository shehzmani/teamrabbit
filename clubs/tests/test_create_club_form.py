from django.test import TestCase
from clubs.models import User
from django import forms
from clubs.forms import CreateClubForm
from django.contrib.auth.hashers import check_password

class TestCreateClubForm(TestCase):
    """Test the create club form"""

    def test_that_club_form_is_valid(self):
        input = {
        'name' : 'a'*10,
        'location' : 'a'*10,
        'description': 'a'*10
        }
    form = CreateClubForm(data=input)
    self.assertTrue(form.is_valid())

    def test_that_club_form_is_invalid(self):
        input = {
        'name': ''
        'location': 'a'*420
        'description': 'a'*420
        }
        form = CreateClubForm(data=input)
        self.assertFalse(form.is_valid())
        
