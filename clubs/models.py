from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.


class User(AbstractUser):
    username = models.CharField(
        max_length=30,
        unique= True,
        validators=[RegexValidator(
            regex=r'^@\w{3,}$',
            message='username must consist of @ followed by at least 3 alphanumericals'
        )]
    )
    first_name = models.CharField(label='First name',max_length=50)
    last_name = models.CharField(label='last name',max_length=50)
    username = models.CharField(label ='username',max_length=50)
    email = models.EmailField(label='Email')
    public_bio = models.CharField(label='Public bio')
    chess_experience_level = models.CharField(label = 'Chess Experience Level') 
