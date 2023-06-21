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
        fields = ('id','project_rel','project_name', 'project_descriotion', 'image_urls', 'audio_urls','videos_urls', 'attachements_urls')


class AllFreelancers(serializers.ModelSerializer):
    # about = serializers.CharField(source='myuser.about')  
    # major = serializers.StringRelatedField(source='major_rel.major_name')

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'about', 'image_url']

class RandomSerial(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'Address', 'country' , 'city', 'email','about','image_url']



class FreelancerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreelancerData
        fields = ['review','image_url','freelancer_rel','major_rel']


class JobsSerializer(serializers.ModelSerializer):
    user_full_name = serializers.SerializerMethodField()

    def get_user_full_name(self, obj):
        users = obj.user_to_jop.all()  # Retrieve all related users
        full_names = [f"{user.first_name} {user.last_name}" for user in users]
        return full_names

    class Meta:
        model = Job
        fields = ['job_id','jop_title','descriotion', 'user_full_name','image_url','min_price','max_price','entry_date' ]

class JobSerializer(serializers.ModelSerializer):
    user_full_name = serializers.SerializerMethodField()

    def get_user_full_name(self, obj):
        users = obj.user_to_jop.all()  # Retrieve all related users
        full_names = [f"{user.first_name} {user.last_name}" for user in users]
        return full_names

    class Meta:
        model = Job
        fields = ['job_id','jop_title','descriotion', 'user_full_name',  'image_url','min_price','max_price','entry_date' ]

