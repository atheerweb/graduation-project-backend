from .models import Category, Course
from graduation.serializers import Get_Category, Get_Top5_Courses
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET'])
def get_category(request,  format = None):
          if request.method == "GET":
          #get all the drinks
             category_name_query =Category.objects.all()
          # serializer them
             serializer =Get_Category(category_name_query, many=True)
          # return them
             return Response(serializer.data)


@api_view(['GET'])
def get_top5_courses(request,  format = None):
          if request.method == "GET":
          #get all the drinks
             top_5_courses_name = Course.objects.all()[:5]
          # serializer them
             serializer = Get_Top5_Courses(top_5_courses_name, many=True)
          # return them
             return Response(serializer.data)