from .models import Category, Course , CourseRegister
from accounts.models import MyUser
from graduation.serializers import Get_Category, Get_Top5_Courses 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from courses.serializer import CoursesSerial , CourseSerial,RandomSerial , CourseSerializerRAN
from random import sample
# Create your views here.

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
        users = MyUser.objects.filter(user_to_course__course_name=course_name)
        full_names = [f"{user.first_name} {user.last_name}" for user in users]
        course_data['user_full_name'] = full_names

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
