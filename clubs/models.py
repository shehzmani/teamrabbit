from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
    max_length = 25,
    unique = True,
    validators=[RegexValidator(
        regex=r'^@\w{3,}$',
        message='username must consist of @ followed by at least 3 alphanumericals'
    )]
)
    first_name = models.CharField(blank=False, max_length=50)
    last_name = models.CharField(blank=False, max_length=50)
    email=models.EmailField(blank=False, unique=True)
    bio = models.CharField(blank= True, max_length=520)

    personal_statement = models.CharField(blank = False, max_length=520)
