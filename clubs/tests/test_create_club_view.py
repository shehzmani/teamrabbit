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
        'password_confirmation': 'Password123',
        }
        self.data = {
        'name': 'The Chess Club',
        'location': 'Kings College London',
        'description': 'A chess club present in Kings College London'

    def test_not_able_to_create_clubs(self):
        self.client.login(username=self.user.username, password="Password123")
        user_count_before = Club.objects.count()
        response = self.client.get(self.url, follow=True)
        user_count_after= Club.objects.count()
        self.assertEqual(user_count_after, user_count_before)
        self.assertEqual(response.status_code, 403)
        
    def test_create_club_url(self):
        self.assertEqual(self.url, '/create_club/')

    def test_make_sure_user_logged_in_to_create(self):
        user_count_before = Club.objects.count()
        redirect_url = reverse('log in')
        response = self.client.post(self.url, self.data, follow=True)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200, fetch_redirect_response=True)
        user_count_after= Club.objects.count()
        self.assertEqual(user_count_after, user_count_before)

    def test_creating_club_is_unsuccessful(self):
        self.client.login(username'@johndoe', password='Password123')
        user_count_before = Club.objects.count()
        self.data['name'] = ""
        response = self.client.post(self.url, self.data, follow=True)
        user_count_after = Club.objects.count()
        self.assertEqual(user_count_after, user_count_before)
        self.assertTemplateUsed(response, 'create_club.html')
