from rest_framework import serializers
from accounts.models import MyUser

class usersSerial(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name','balance','image_url']