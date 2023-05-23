from .models import Job
from graduation.serializers import Get_Jops
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def get_jops(request,  format = None):
          if request.method == "GET":
          #get all the drinks
             jobs_query =Job.objects.all()
          # serializer them
             serializer =Get_Jops(jobs_query, many=True)
          # return them
             return Response(serializer.data)