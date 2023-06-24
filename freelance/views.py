from re import I
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from freelance.models import projects
from .serializer import ProjectsSerializer,JobsSerializer , JobSerializer , FreelancerDataSerializer , All_Major
from django.views.decorators.http import require_http_methods
from graduation.serializers import Userserializer, Roleserializer, UserRolesSerializers 
from django.http import JsonResponse
from accounts.models import MyUser
from users.models import Permission, Role, UserRoles
from freelance.models import Job,UserApplyJobs, Major, FreelancerData
from django.contrib.auth.models import User
from .serializer import AllFreelancers, RandomSerial
from graduation.serializers import UserRolesSerializers
from django.http import JsonResponse
from django.http import HttpRequest
from random import sample
from rest_framework.authentication import SessionAuthentication, BasicAuthentication ,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import viewsets
# from graduation.permissons import IsOwnerOrReadOnly
# from .permission import IsOwnerOrReadOnlyForJob

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
      freelancer_users = MyUser.objects.filter(role_to_user=freelancer_roles)
      
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
            'image_url': f"{freelancer.image_url} ",
            'name': f"{freelancer.about} ",
            'projects': projects_data
         }
         return Response(freelancer_data)
      except MyUser.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def top_5_freelancers(request):
   if request.method == 'GET':
      freelancer_roles = Role.objects.get(role_id=2)
      freelancer_users = MyUser.objects.filter(role_to_user=freelancer_roles)[:5]
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

         # Get the major names for the freelancer
         majors = freelancer.major_to_user.all()
         major_names = [major.major_name for major in majors]

         freelancer_data = {
               'name': f"{freelancer.first_name} {freelancer.last_name}",
               'about': freelancer.about,
               'major': major_names,
               'projects': projects_data,
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

@api_view(['GET'])
def get_job(request, id, format=None):
    if request.method == "GET":
        jobs_name_query = Job.objects.get(job_id=id)
        serializer = JobSerializer(jobs_name_query)
        return Response(serializer.data)
        # return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def post(request):
         if request.method == 'POST':
            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# viewsets for jobs include post, get, put, delete and exact filter
class viewsets_job(viewsets.ModelViewSet):
   queryset = Job.objects.all()
   serializer_class = JobSerializer
   filter_backends =[filters.DjangoFilterBackend,]
   filterset_fields = ['jop_title','major_rel']
#  authentication_classes = [TokenAuthentication,]
   # permission_classes = [IsOwnerOrReadOnlyForJob]



# viewsets for projects include post, get, put, delete and exact filter
class viewsets_project(viewsets.ModelViewSet):
   queryset = projects.objects.all()
   serializer_class = ProjectsSerializer
   filter_backends =[filters.DjangoFilterBackend,]
   filterset_fields = ['project_name','project_descriotion']
   # permission_classes = [IsOwnerOrReadOnly]

# filter by major name
@api_view()
@permission_classes([AllowAny])
def major_filter(request, format=None):
    queryset = Job.objects.all()
    major = request.query_params.get('major_rel__major_name', None)
    if major: 
        queryset = queryset.filter(major_rel__major_name__contains=major)
        if len(queryset) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    serializer = JobsSerializer(queryset, many=True)
    data = serializer.data
    return Response(data)
  
# Filter by Job title 

@api_view()
@permission_classes([AllowAny])
def job_filter(request, format=None):
    queryset = Job.objects.all()
    job_name = request.query_params.get('jop_title', None)
    if job_name:
           queryset = queryset.filter(jop_title__contains=job_name)
           if len(queryset) == 0:
               return Response(status=status.HTTP_404_NOT_FOUND)
         
    serializer = JobsSerializer(queryset, many=True)
    data = serializer.data
    return Response(data)
  
#Filter by freelancer name

@api_view()
@permission_classes([AllowAny])
def freelancer_filter(request, format=None):
    queryset = FreelancerData.objects.all()
    freelancer_name = request.query_params.get('freelancer_rel__first_name', None)
    if freelancer_name:
           queryset = queryset.filter(freelancer_rel__first_name__contains=freelancer_name)
           if len(queryset) == 0:
               return Response(status=status.HTTP_404_NOT_FOUND)
         
    serializer = FreelancerDataSerializer(queryset, many=True)
    data = serializer.data

   #  Retrieve and append user first and last name

   #  for freelancer_data in data:
   #      name = freelancer_data['freelancer_rel']
   #      users = MyUser.objects.filter(freelancer_rel__first_name=name)
   #      full_names = [f"{user.first_name} {user.last_name}" for user in users]
   #      freelancer_data['user_full_name'] = full_names

    return Response(data)

   #  for freelancer_data in data:
   #      freelancer_rel = freelancer_data['freelancer_rel']
   #      users = MyUser.objects.filter(id=freelancer_rel.id, first_name=freelancer_rel.first_name)
   #      full_names = [f"{user.first_name} {user.last_name}" for user in users]
   #      freelancer_data['user_full_name'] = full_names

   #  return Response(data)

# filter by freelancer major 
@api_view()
@permission_classes([AllowAny])
def freelancer_major_filter(request, format=None):
    queryset = FreelancerData.objects.all()
    freelancer_name = request.query_params.get('major_rel__major_name', None)
    if freelancer_name:
           queryset = queryset.filter(major_rel__major_name__contains=freelancer_name)
           if len(queryset) == 0:
               return Response(status=status.HTTP_404_NOT_FOUND)
         
    serializer = FreelancerDataSerializer(queryset, many=True)
    data = serializer.data

    return Response(data)
  
@api_view(['GET'])
def get_all_major(request,  format = None):
        if request.method == "GET":
            major_name_query =Major.objects.all()
            serializer =All_Major(major_name_query, many=True)
            return Response(serializer.data)
