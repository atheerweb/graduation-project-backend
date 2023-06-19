from django.db import models
from datetime import datetime
from accounts.models import MyUser
from django.utils import timezone

# Create your models here.
class FreelancerTransaction(models.Model):
    freelancer_rel = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    transaction_name_f = models.CharField(max_length=255)
    transaction_date_f = models.DateTimeField(default=datetime.now)

class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    major_name = models.CharField(max_length=1000)
    user_to_Major = models.ManyToManyField('accounts.MyUser',through='FreelancerData', related_name='major_to_user')

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    jop_title = models.CharField(max_length=255)
    descriotion = models.CharField(max_length=1000)
    major_rel = models.ForeignKey(Major ,on_delete=models.CASCADE, null=True)
    image_url = models.CharField(max_length=2000 , null=True)
    min_price = models.FloatField(max_length=100 , null=True)
    max_price = models.FloatField(max_length=100 , null=True)
    entry_date = models.DateTimeField(default=timezone.now)
    user_to_jop = models.ManyToManyField('accounts.MyUser',through='UserApplyJobs',related_name='jop_to_user')

class UserApplyJobs(models.Model):
    jop_rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user_freelancer_rel = models.ForeignKey(Job, on_delete=models.CASCADE)
    owner = models.BooleanField(default=False)

class projects(models.Model):
    project_rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    project_descriotion = models.CharField(max_length=1000)
    image_urls = models.CharField(max_length=1000)
    audio_urls = models.CharField(max_length=1000)
    videos_urls = models.CharField(max_length=1000)
    attachements_urls = models.CharField(max_length=1000)



class FreelancerData(models.Model):
    freelancer_rel = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    review = models.FloatField(max_length=5)
    image_url = models.CharField(max_length=2000 , null=True)
    major_rel = models.ForeignKey(Major ,on_delete=models.CASCADE , null=True)
