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

class Role (models.Model):
    Role_id = models.AutoField(primary_key=True)
    Role_name = models.CharField(max_length=45)


class Permission (models.Model):
    Permission_ID = models.AutoField(primary_key=True)
    Permission_Name = models.CharField(max_length=45)
    # Role_Role_ID = models.ForeignKey(Role, on_delete=models.CASCADE)
