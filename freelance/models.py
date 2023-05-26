from django.db import models
from datetime import datetime
from accounts.models import MyUser
# Create your models here.
class FreelancerTransaction(models.Model):
    freelancer_rel = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    transaction_name_f = models.CharField(max_length=255)
    transaction_date_f = models.DateTimeField(default=datetime.now)

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    jop_title = models.CharField(max_length=255)
    descriotion = models.CharField(max_length=1000)
    jop_to_user= models.ManyToManyField('accounts.MyUser',through='UserApplyJobs')


class UserApplyJobs(models.Model):
    jop_rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    user_freelancer_rel = models.ForeignKey(Job, on_delete=models.CASCADE)

class projects(models.Model):
    project_rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    project_descriotion = models.CharField(max_length=1000)
    image_urls = models.CharField(max_length=1000)
    audio_urls = models.CharField(max_length=1000)
    videos_urls = models.CharField(max_length=1000)
    attachements_urls = models.CharField(max_length=1000)