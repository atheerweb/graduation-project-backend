from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from django.views.decorators.http import require_http_methods

from graduation.serializers import Userserializer, Roleserializer, UserRolesSerializers
from django.http import JsonResponse
from .models import User, Permission, Role, UserRoles


# Create your views here.


@api_view(['GET', 'POST'])
def user_list(request, format=None):

    # get all the data
    # serialize them
    # return json

    # check up -----> request GET
    if request.method == 'GET':
        query_user = User.objects.all()
        serializer = Userserializer(query_user, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            id = serializer.data['user_id']
            query_role = Role.objects.filter(role_name=request.data['role'])
            serializer3 = Roleserializer(query_role, many=True)
            print("role_id:", serializer3.data[0]['role_id'])
            data_dic = {'user_rel': id,
                        'role_rel': serializer3.data[0]['role_id']}
            serializer2 = UserRolesSerializers(data=data_dic)
            if serializer2.is_valid():
                serializer2.save()
            return Response({'user_info': [serializer.data], 'relation_info': [serializer2.data]}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def role_list(request, role, format=None):

    if request.method == 'GET':
        query_role = Role.objects.filter(role_name=role)
        serializer = Roleserializer(query_role, many=True)
        if serializer.data == []:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.data)


@api_view(['GET', 'POST'])
def UserRoles_list(request, format=None):

    if request.method == 'GET':
        query_user_role = UserRoles.objects.all()
        serializer = UserRolesSerializers(query_user_role, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = UserRolesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@require_http_methods(["GET"])
def get_id_by_name(request):
    name = request.GET.get('role_name')
    if name:
        try:
            record = Role.objects.get(name=name)
            return JsonResponse({'id': record.id})
        except Role.DoesNotExist:
            return JsonResponse({'error': 'Record not found'})
    else:
        return JsonResponse({'error': 'Name parameter not provided'})
