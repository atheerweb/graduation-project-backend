from django.db import models
from datetime import datetime
# Create your models here.
from accounts.models import MyUser




class Role (models.Model):
    role_id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255)
    role_to_user = models.ManyToManyField('accounts.MyUser', through='UserRoles')
    role_to_per = models.ManyToManyField('Permission', through='RolePermetion')

    def __str__(self):
        return str(self.role_id)


class Permission (models.Model):
    permission_id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=255)
    per_to_role = models.ManyToManyField('Role', through='RolePermetion')

    def __str__(self):
        return str(self.permission_id)


class UserRoles(models.Model):
    user_rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    role_rel = models.ForeignKey(Role, on_delete=models.CASCADE)


class RolePermetion(models.Model):
    permeion_rel = models.ForeignKey(Permission, on_delete=models.CASCADE)
    role_rel = models.ForeignKey(Role, on_delete=models.CASCADE)


class Transaction(models.Model):
    user_fore =  models.ForeignKey(MyUser, on_delete=models.CASCADE)
    course_fore = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    transaction_name = models.CharField(max_length=255)
    transaction_date = models.DateTimeField(default=datetime.now)
