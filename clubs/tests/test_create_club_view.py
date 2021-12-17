from django.test import TestCase
from clubs.models import User
from clubs.models import Club
from django.urls import reverse
from django.contrib.auth.hashers import check_password

class TestCreateClubView(TestCase):
    """Test the create club view"""

    def setUp(self):
        self.url = reverse('create_club')
        self.form_input = {
        'first_name': 'Jane',
        'last_name': 'Doe',
        'username': '@janedoe',
        'email': "janedoe@example.org",
        'new_password': 'Password123',
        'password_confirmation': 'Password123'
        }

    def test_get_create_club_function(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_club.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, CreateClubForm))
        self.assertFalse(form.is_bound)
        
    def test_create_club_url(self):
        self.assertEqual(self.url, '/create_club/')
