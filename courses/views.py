from .models import Category, Course
from graduation.serializers import Get_Category, Get_Top5_Courses
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from courses.serializer import CoursesSerial , CourseSerial,RandomSerial
from random import sample
# Create your views here.

@api_view(['GET'])
def get_courses(request,  format = None):
         if request.method == "GET":
         #get all the drinks
            courses_name_query =Course.objects.all()
         # serializer them
            serializer =CoursesSerial(courses_name_query, many=True)
         # return them
            return Response(serializer.data)
         
@api_view(['GET'])
def get_course(request , id , format = None):
         #get all the drinks
         try:
             course_query = Course.objects.get(pk=id)
         except Course.DoesNotExist:
             return Response(status=status.HTTP_404_NOT_FOUND)

         if request.method == 'GET':
             serializer = CourseSerial(course_query)
             return Response(serializer.data)


@api_view(['GET'])
def get_top5_courses(request,  format = None):
    courses = Course.objects.values('course_name', 'price','duration')
    random_courses = sample(list(courses), 5)  # Get random 5 users from the queryset
    serializer = RandomSerial(random_courses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_category(request,  format = None):
          if request.method == "GET":
             category_name_query =Category.objects.all()
             serializer =Get_Category(category_name_query, many=True)
             return Response(serializer.data)
