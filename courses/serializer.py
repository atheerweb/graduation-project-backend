from rest_framework import serializers
from users.models import  UserRoles, Role
from courses.models import Category, Course
from freelance.models import Job
from rest_framework import serializers
from accounts.models import MyUser
from django.contrib.auth.models import User


class CourseSerial(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = ( 'course_name', 'price','duration' )
class CoursesSerial(serializers.ModelSerializer):
    class Meta:
        model = Course 
        fields = ( 'course_name', 'price','duration' )

class Category(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name')

class RandomSerial(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'price','duration']