from rest_framework import serializers
from users.models import User, UserRoles, Role


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
