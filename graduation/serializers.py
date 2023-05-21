from rest_framework import serializers
from users.models import User, UserRoles, Role 
from courses.models import Category,Course
from freelance.models import Job


class Userserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'gender', 'birth_date',
                  'country', 'city', 'Street', 'email_address', 'password',]


class Roleserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['role_id', 'role_name']


class UserRolesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = ['user_rel', 'role_rel']


class Get_Category(serializers.ModelSerializer):
          class Meta:
                model = Category
                fields =['category_name']

class Get_Top5_Courses(serializers.ModelSerializer):
          class Meta:
                model = Course
                fields =['course_name', 'price', 'duration']


class Get_Jops(serializers.ModelSerializer):
          class Meta:
                model = Job
                fields =['jop_title','descriotion']