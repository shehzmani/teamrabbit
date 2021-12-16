from django.test import TestCase
from clubs.models import User
from django.core.excpetions import ValidationError

class TestUserModelCase(TestCase):
    """Test all aspects of a user."""

    # Helper functions
    # Generic assertions
    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except (ValidationError):
            self.fail("Test user should be valid")

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

    #Test set up
    def setUp(self):
        self.user = User.objects.create_user(
            'johndoe',
            first_name = 'John',
            last_name = 'Doe',
            email = 'johndoe@example.org'
            password='Password123',
        )

    def test_valid_user(self):
        self._assert_user_is_valid()

    # Test Username
    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._asser_user_is_invalid()

    def test_username_max_chars_30_chars(self):
        self.user.username = 'a'*30
        self._assert_user_is_valid()

    def test_username_cannot_be_31_chars_long(self):
        self.user.username = 'a'*31
        self._assert_user_is_invalid()

    def test_username_must_be_longer_than_2_characters(self):
        self.user.username = 'jo'
        self._assert_user_is_invalid()

    def test_username_must_be_unique(self):
        User.objects.create_user(
        'janedoe'
        first_name = 'Jane',
        last_name = 'Doe',
        email = 'janedoe@example.org',
        Password = 'Password123',
        )
        self.user.username = 'janedoe'
        self._assert_user_is_invalid()

    def test_username_must_contain_only_alphanumericals(self):
        self.user.username = '@john1!doe'
        self._assert_user_is_invalid()

    def test_username_can_contain_numbers(self):
        self.user.username = 'john1doe2'
        self._assert_user_is_valid()

    #Test first name
    def test_first_name_cannot_be_blank(self):
        self.user.first_name=''
        self._assert_user_is_invalid()

    def test_first_name_not_unique(self):
        User.objects.create_user(
            'janedoe',
            first_name = 'Jane',
            last_name = 'Doe',
            email = 'janedoe@example.org',
            password = 'Password123',
        )
        self.user.first_name = 'Jane'
        self._assert_user_is_valid()

    def test_first_name_max_chars_50(self):
        self.user.first_name = 'b'*50
        self._assert_user_is_valid()

    def test_first_name_cannot_be_51_chars_long(self):
        self.user.first_name = b*51
        self._assert_user_is_invalid()

    #Test last name
    def test_last_name_cannot_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()

    def test_last_name_not_unique(self):
        User.objects.create_user(
        'janedoe',
        first_name = 'Jane',
        last_name = 'Doe',
        email = 'janedoe@example.org',
        password = 'Password123',
        )
        self.user.last_name = 'Doe'
        self._assert_user_is_valid()

    def test_last_name_max_chars_50(self):
        self.user.last_name = 'b'*50
        self._assert_user_is_valid()

    def test_last_name_cannot_be_51_chars_long(self):
        self.user.last_name = 'b'*51
        self._assert_user_is_invalid()

    #Test email
    def test_email_is_unique(self):
        User.objects.create_user(
        'janedoe',
        first_name = 'Jane',
        last_name = 'Doe',
        email = 'janedoe@example.org',
        password = 'Password123',
        )
        self.user.email = 'janedoe@example.org'
        self._assert_user_is_invalid()

    def test_email_has_to_have_at_symbol(self):
        self.user.email = 'johndoeexample.org'
        self._assert_user_is_invalid()

    def test_email_cannot_have_more_than_one_at_symbol(self):
        self.user.email = 'johndoe@@example.org'
        self._assert_user_is_invalid()

    def test_email_can_have_special_characters_before_at(self):
        self.user.email = 'john.doe!@example.org'
        self._assert_user_is_valid()

    def test_email_cannot_have_special_characters_after_at(self):
        self.user.email = 'johndoe@!example.org'
        self._assert_user_is_invalid()

    def test_email_cannot_have_more_than_one_dot_after_at_symbol(self):
        self.user.email = 'johndoe@example..org'
        self._asser_user_is_invalid()
