from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        label = 'Username'
        max_length=30,
        unique= True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='username must consist of @ followed by at least 3 alphanumericals'
        )]
    )

    first_name = models.CharField(
    label='First name',
    blank=False,
    max_length=50)

    last_name = models.CharField(
    label='last name',
    blank=False,
    max_length=50
    )

    username = models.CharField(
    label ='username',
    blank=False,
    max_length=50
    )

    email = models.EmailField(
    label='Email',
    blank=False,
    max_length=300
    )

    personalStatement = models.TextField(
    label='Personal Statement',
    blank=False,
    max_length=600
    )

    chessExperienceChoices = (
    ('basic', 'BASIC')
    ('intermediate', 'INTERMEDIATE')
    ('expert', 'EXPERT')
    )

    chessExperience = models.CharField(
    label = 'Chess Experience'
    max_length =12,
    choices = chessExperienceChoices,
    default = 'basic',
    )

    def gravatar(self, size=120):
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url
