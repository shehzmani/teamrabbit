from django.db import models

class Applicant(models.Model):
    form_id = models.AutoField(primary_key=True)
    name = models.TextField()
    email = models.TextField()
    public_bio = models.TextField()
    chess_experience = models.TextField()
    personal_statement = models.TextField()
    aim_club = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
