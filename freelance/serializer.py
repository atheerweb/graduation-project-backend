from rest_framework import serializers
from .models import projects
from accounts.models import MyUser
from users.models import UserRoles
from freelance.models import Job, FreelancerData

class Top5(serializers.ModelSerializer):
    class Meta: 
        model = UserRoles 
        fields = ['user_rel', 'role_rel']
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ('project_rel','project_name', 'project_descriotion', 'image_urls', 'audio_urls','videos_urls', 'attachements_urls')


class AllFreelancers(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username','first_name', 'last_name', 'email', 'about',]

class RandomSerial(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username','first_name', 'last_name', 'Address', 'country' , 'city', 'email','about']

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job_id','jop_title','descriotion','major_rel']
        
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['job_id','jop_title','descriotion']

class FreelancerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerData
        fields = ['review','image_url','freelancer_rel','major_rel']


