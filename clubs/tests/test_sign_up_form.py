from django.test import TestCase
from clubs.models import User
from django.contrib.auth.hashers import check_password
from django import forms
from clubs.forms import SignUpForm

class SignUpFormTestCase(TestCase):
    def setUp(self):
        self.form_input = {
        'first_name' : 'John',
        'last_name' : 'Doe',
        'username' : '@johndoe',
        'email' : 'johndoe@example.org',
        'new_password' : 'Password123'
        'password_confirmation' : 'Password123'
        }

    def test_valid_sign_up_form(self):
        form = SignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_contains_necessary_fields(self):
        form = SignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)

        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))

        self.assertIn('new_password', form.fields)
        new_password_widget = form.fields['new password'].new_password_widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
        scd_password_widget = form.fields['password confirmation'].widget
        self.assertTrue(isinstance(scd_password_widget, forms.PasswordInput))

    def test_form_uses_modelvalidation(self):
        self.form_input['username'] = 'bad user'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_contain_uppercase_char(self):
        self.form_input['new_password'] = 'password123'
        self.form_input['password_confirmation'] = 'password123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_contain_lower_case(self):
        self.form_input['new_password'] = 'PASSWORD123'
        self.form_input['password_confirmation'] = 'PASSWORD123'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_must_contain_number(self):
        self.form_input['new_password'] = 'Password'
        self.form_input['password_confirmation'] = 'Password'
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_password_and_confirmation_identical(self):
        self.form_input['password_confirmation'] = "Mismatched Password"
        form = SignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_form_saves(self):
        user_count_before = User.objects.count()
        form = SignUpForm(data=self.form_input)
        form.save()
        user_count_after = User.objects.count()
        self.assertEqual(user_count_after, user_count_before+1)
        user = User.objects.get(username = '@johndoe')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'johndoe@example.org')
        is_password_valid = check_password('Password123', user.password)
        self.assertTrue(is_password_valid)
