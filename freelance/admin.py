from django.contrib import admin
from .models import FreelancerTransaction, Job, UserApplyJobs
# Register your models here.
admin.site.register(FreelancerTransaction)
admin.site.register(Job)
admin.site.register(UserApplyJobs)
