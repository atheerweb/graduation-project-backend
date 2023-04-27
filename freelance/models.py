from django.db import models
from datetime import datetime
from users.models import User
# Create your models here.
class FreelancerTransaction(models.Model):
    freelancer_rel = models.ForeignKey(User,on_delete=models.CASCADE)
    transaction_name_f = models.CharField(max_length=255)
    transaction_date_f = models.DateTimeField(default=datetime.now)

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    jop_title = models.CharField(max_length=255)
    descriotion = models.CharField(max_length=1000)
    jop_to_user= models.ManyToManyField('users.User',through='UserApplyJobs')

class UserApplyJobs(models.Model):
    jop_rel = models.ForeignKey(User, on_delete=models.CASCADE)
    user_freelancer_rel = models.ForeignKey(Job, on_delete=models.CASCADE)