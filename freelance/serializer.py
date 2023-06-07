from rest_framework import serializers
from .models import projects
from accounts.models import MyUser
from users.models import UserRoles
from freelance.models import Job

class Top5(serializers.ModelSerializer):
    class Meta: 
        model = UserRoles 
        fields = ['user_rel', 'role_rel']
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ('project_name', 'project_descriotion', 'image_urls', 'videos_urls', 'attachements_urls')


class AllFreelancers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'email']

class RandomSerial(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'Address', 'country' , 'city', 'email']

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job_id','jop_title','descriotion']