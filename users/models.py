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

    def __str__(self):
        return str(self.user_id)


class Role (models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=45)
    role_has_user = models.ManyToManyField(User, null=True)

    def __str__(self):
        return str(self.role_id)


class Permission (models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=45)
    permission_has_role = models.ManyToManyField(Role, null=True)

    def __str__(self):
        return str(self.permission_id)


class UserRoles(models.Model):
    user_rel = models.ForeignKey(User, on_delete=models.CASCADE)
    role_rel = models.ForeignKey(Role, on_delete=models.CASCADE)

class RolePermetion(models.Model):
    permeion_rel = models.ForeignKey(Permission, on_delete=models.CASCADE)
    role_rel = models.ForeignKey(Role, on_delete=models.CASCADE)
