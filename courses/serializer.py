from rest_framework import serializers
from users.models import  UserRoles, Role

from courses.models import Category, Course
from freelance.models import Job
from rest_framework import serializers
from accounts.models import MyUser
from django.contrib.auth.models import User

class userser(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name','last_name']

class CourseSerial(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = [ 'course_name', 'price','duration' ]
class CoursesSerial(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = ( 'course_name', 'price','duration'  )

class Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name')

class RandomSerial(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_id','course_name', 'price','duration']




class CourseSerializerRAN(serializers.ModelSerializer):
    user_full_name = serializers.SerializerMethodField()

    def get_user_full_name(self, obj):
        users = obj.user_to_course.all()  # Retrieve all related users
        full_names = [f"{user.first_name} {user.last_name}" for user in users]
        return full_names

    class Meta:
        model = Course
        fields = ['course_id', 'course_name', 'price', 'duration', 'user_full_name' ]