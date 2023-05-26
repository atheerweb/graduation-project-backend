from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(max_length=9, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    Address = models.CharField(max_length=255, blank=True, null=True)
    user_to_role = models.ManyToManyField(
        'users.Role', through='users.UserRoles')
    user_to_course = models.ManyToManyField(
        'courses.Course', through='courses.CourseRegister')
    user_to_jop = models.ManyToManyField(
        'freelance.Job', through='freelance.UserApplyJobs')

    def __str__(self):
        return self.username
