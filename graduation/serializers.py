from rest_framework import serializers
from users.models import User, UserRoles, Role 
from courses.models import Category,Course
from freelance.models import Job
from rest_framework import serializers
from accounts.models import MyUser
from django.contrib.auth.models import User


from django.contrib.auth import get_user_model
User = get_user_model()
# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email','gender','birth_date','country','city','Address')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'username', 'email', 'password','gender','birth_date','country','city','Address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = MyUser.objects.create(username = validated_data['username'], 
        email = validated_data['email'], 
        password = validated_data['password'],
        gender = validated_data['gender'], 
        birth_date = validated_data['birth_date'],
         country = validated_data['country'],
        city =  validated_data['city'],
        Address = validated_data['Address'],)

        return user

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