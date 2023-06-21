import courses
from courses import serializer
from .models import Category, Course , CourseRegister
from accounts.models import MyUser
from graduation.serializers import Get_Category, Get_Top5_Courses 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from courses.serializer import CoursesSerial , CourseSerial,RandomSerial , CourseSerializerRAN, CourseSerial_url, CateogrySerial
from random import sample
from django_filters import rest_framework as filters
# from courses.permission import IsOwnerOrReadOnly

# Create your views here.

# Filter by Courses name 

@api_view()
@permission_classes([AllowAny])
def get_courses(request, format=None):
    queryset = Course.objects.all()
    course_name_v = request.query_params.get('course_name', None)
    if course_name_v:
        queryset = queryset.filter(course_name__contains=course_name_v)
        if len(queryset) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CoursesSerial(queryset, many=True)
    data = serializer.data

    # Retrieve and append user first and last name
    for course_data in data:
        course_name = course_data['course_name']
        users = MyUser.objects.filter(course_to_user__course_name=course_name)
        full_names = [f"{user.first_name} {user.last_name}" for user in users]
        course_data['user_full_name'] = full_names

    return Response(data)

# Filter by category 
@api_view()
@permission_classes([AllowAny])
def category_filter(request, format=None):
    queryset = Course.objects.all()
    category_name = request.query_params.get('cat_has_courses__category_name', None)
    if category_name:
           queryset = queryset.filter(cat_has_courses__category_name__contains=category_name)
           if len(queryset) == 0:
               return Response(status=status.HTTP_404_NOT_FOUND)
         
    serializer = CateogrySerial(queryset, many=True)
    data = serializer.data
    return Response(data)

@api_view(['GET'])
def get_course(request , id , format = None):
        #get all the drinks
        try:
            course_query = Course.objects.get(pk=id)
            CourseRegister_q = CourseRegister.objects.filter(Course_rel=course_query.course_id)
            user_nameuniq_id=CourseRegister_q.get().user_rel
            user_q = MyUser.objects.filter(username= user_nameuniq_id)
            
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CourseSerial(course_query)
            
            serializer.data.update({'username':user_q.get().username})

            sel = dict(serializer.data)
            sel['username']=user_q.get().username
            sel['name']=user_q.get().first_name + " "+ user_q.get().last_name
            return Response(sel)



# @api_view(['GET'])
# def get_top5_courses(request,  format = None):
#     courses = Course.objects.values('course_id','course_name', 'price','duration')
#     random_courses = sample(list(courses), 5)  # Get random 5 users from the queryset
#     serializer = RandomSerial(random_courses, many=True)
#     print(random_courses[0]['course_id'])
#     l =[]
#     for v in random_courses:
#          user_id = v.id
#          l.append(user_id)
#     #CourseRegister_q = CourseRegister.objects.filter(Course_rel=random_courses['course_id'])
#     #print(CourseRegister_q.all())

#     #user_nameuniq_id=CourseRegister_q.get().user_rel
#     #user_q = MyUser.objects.filter(username= user_nameuniq_id)

#     return Response(serializer.data)

@api_view(['GET'])
def get_suggested_courses(request, format=None):
    courses = Course.objects.order_by('?')[:3]
    serializer = CourseSerializerRAN(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_category(request,  format = None):
        if request.method == "GET":
            category_name_query =Category.objects.all()
            serializer =Get_Category(category_name_query, many=True)
            return Response(serializer.data)



@api_view(['GET'])
def get_top5_courses(request, format=None):
    courses = Course.objects.order_by('?')[:5]
    serializer = CourseSerializerRAN(courses, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def get_top5_courses(request, format=None):
    courses = Course.objects.all()
    random_courses = sample(list(courses), 5)
    serializer = CourseSerializerRAN(random_courses, many=True)
    return Response(serializer.data)

# Viewsets for Courses 

from rest_framework import viewsets
class viewsets_courses(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerial
    filter_backends =[filters.DjangoFilterBackend,]
    filterset_fields = ['course_name','price']
    # permission_classes = [IsOwnerOrReadOnly]


# Find Course
@api_view(['GET'])
def find_course(request):
    courses = Course.objects.filter(course_name = request.data['course_name'])
                                    # price = request.data['price']
    serializer = CoursesSerial(courses,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_course_url(request , id , format = None):
        #get all the drinks
        try:
            course_query = Course.objects.get(pk=id)
            CourseRegister_q = CourseRegister.objects.filter(Course_rel=course_query.course_id)
            user_nameuniq_id=CourseRegister_q.get().user_rel
            user_q = MyUser.objects.filter(username= user_nameuniq_id)

        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = CourseSerial_url(course_query)

            return Response(serializer.data)
