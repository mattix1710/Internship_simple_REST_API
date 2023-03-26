from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny

from django.contrib.auth import authenticate, login, logout

# created models
from master_CS.models import *
from .serializers import CourseSerializer, StudentSerializer, StudentCoursesSerializer, UserBasicInfoSerializer

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def getCourses(request: Request):
    # print(request.content_type)
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudentsCourses(request):
    assignments = CourseAssignment.objects.all()
    serializer = StudentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getCourseDetails(request):
    hello =''
    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def getMyCourses(request):
    
    courses = CourseAssignment.objects.filter(student = request.user.email)
    serializer = StudentCoursesSerializer(courses)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
    # print(request.user.data)
    
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def aboutMe(request):
    my_info = User.objects.get(email = request.user.email)
    serializer = UserBasicInfoSerializer(my_info)
    return Response(serializer.data, status=status.HTTP_200_OK)