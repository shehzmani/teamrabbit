from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique= True,
        validators=[RegexValidator(
        regex=r'^\w{3,}$'),
        ],
    )

    first_name = models.CharField(
    blank=False,
    max_length=50,
    validators=[RegexValidator(
    regex=r'^[a-zA-Z]{1,}$'),
    ],
    )

    last_name = models.CharField(
    blank=False,
    max_length=50,
    validators=[RegexValidator(
    regex=r'^[a-zA-Z]{1,}$'),
    ],
    )

    email = models.EmailField(
    blank=False,
    max_length=300,
    )

    personalStatement = models.TextField(
    blank=False,
    max_length=600,
    )

    def gravatar(self, size=120):
        gravatar_object = Gravatar(self.email)
        gravatar_url = gravatar_object.get_image(size=size, default='mp')
        return gravatar_url
