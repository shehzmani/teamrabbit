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

class Club(models.Model):
    name = models.CharField(blank=True, max_length=60, unique=True)
    location = models.CharField(blank=True, max_length=60, unique=False)
    descrption = models.CharField(blank=True, max_length=250, unique=False)
    time_created = models.DateTimeField(auto_now_add=True, blank=False)

    class Meta:
        ordering = ['-time_created']

class Member(models.Model):
    """Model that represents members of the chess club and their significant roles in the clubs"""
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isOwner = BooleanField(default=True)
    isOfficer= BooleanField(default=False)
