from django.db import models
from datetime import datetime
from accounts.models import MyUser

# Create your models here.


class SupportTicket (models.Model):

    Ticket_id = models.AutoField(primary_key=True)
    status = models.BooleanField(default=False)
    # 1,000 characters is between 142 words and 250 words
    description = models.CharField(max_length=1000)
    date_time = models.DateTimeField(default=datetime.now)
    user_re = models.OneToOneField(MyUser, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.Ticket_id)
