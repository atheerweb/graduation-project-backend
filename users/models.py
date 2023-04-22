from django.db import models

# Create your models here.


class User (models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField(max_length=9)
    country = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    Street = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=40)
