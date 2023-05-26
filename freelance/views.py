from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from freelance.models import projects
from .serializer import ProjectsSerializer,JobsSerializer
from django.views.decorators.http import require_http_methods
from graduation.serializers import Userserializer, Roleserializer, UserRolesSerializers
from django.http import JsonResponse
from accounts.models import MyUser
from users.models import Permission, Role, UserRoles
from freelance.models import Job,UserApplyJobs
from django.contrib.auth.models import User
from .serializer import AllFreelancers, RandomSerial
from graduation.serializers import UserRolesSerializers
from django.http import JsonResponse
from django.http import HttpRequest
from random import sample


# Create your views here.


@api_view(['GET', 'POST'])
def user_list(request, format=None):
   # get all the data
   # serialize them
   # return json

   # check up -----> request GET
   if request.method == 'GET':
      query_user = MyUser.objects.all()
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
         return Response({'user_info': [serializer.data], 'relation_info': [serializer2.data]},
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_freelancers(request):
   if request.method == 'GET':
      freelancer_roles = Role.objects.get(role_id=2)
      freelancer_users = MyUser.objects.filter(user_to_role=freelancer_roles)
      serializer = AllFreelancers(freelancer_users, many=True)
      return Response(serializer.data)


@api_view(['GET'])
def get_freelancer_with_projects(request, id, format=None):
   if request.method == 'GET':
      try:
         freelancer = MyUser.objects.get(username=id)
         projects_query = projects.objects.filter(project_rel=freelancer)
         projects_serializer = ProjectsSerializer(projects_query, many=True)
         projects_data = projects_serializer.data
         freelancer_data = {
            'name': f"{freelancer.first_name} {freelancer.last_name}",
            'projects': projects_data
         }
         return Response(freelancer_data)
      except MyUser.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def top_5_freelancers(request):
   if request.method == 'GET':
      freelancer_roles = Role.objects.get(role_id=2)
      freelancer_users = MyUser.objects.filter(user_to_role=freelancer_roles)[:5]
      serializer = AllFreelancers(freelancer_users, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def role_list(request, role, format=None):
   if request.method == 'GET':
      query_role = Role.objects.filter(role_name=role)
      serializer = Roleserializer(query_role, many=True)
      if serializer.data == []:
         return Response(status=status.HTTP_404_NOT_FOUND)

      return Response(serializer.data)


@api_view(['GET'])
def job_freelancers(request, role, format=None):
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


@api_view(['GET'])
def get_random_users(request):
   users = MyUser.objects.values('first_name', 'last_name', 'Address', 'country', 'city', 'email')
   random_users = sample(list(users), 5)  # Get random 5 users from the queryset
   serializer = RandomSerial(random_users, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def get_freelancer_with_projects(request, id, format=None):
   if request.method == 'GET':
      try:
         freelancer = MyUser.objects.get(username=id)
         projects_query = projects.objects.filter(project_rel=freelancer)
         projects_serializer = ProjectsSerializer(projects_query, many=True)
         projects_data = projects_serializer.data
         freelancer_data = {
               'name': f"{freelancer.first_name} {freelancer.last_name}",
               'projects': projects_data
         }
         return Response(freelancer_data)
      except MyUser.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_jobs(request,  format = None):
         if request.method == "GET":
            jobs_name_query =Job.objects.all()
            serializer =JobsSerializer(jobs_name_query, many=True)
            return Response(serializer.data)




