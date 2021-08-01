from django.shortcuts import render
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer 
from nsapp.models import Instructor
from nsapp.serializers import InstructorSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser , BasePermission
from rest_framework.authentication import BaseAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# Create your views here.
'''
users = User.objects.all()
for user in users:
    token = Token.objects.get_or_create(user=user)
    #print(token)'''

class WriteByAdminOnlyPermission(BasePermission):    #custom adminacess
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True

        if request.method == 'POST' or request.method == 'PUT' or request.method =='DELETE':
            if user.is_superuser:
                return True
            return False


class InstructorListView(generics.ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

'''
class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes=[IsAuthenticated,WriteByAdminOnlyPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer'''

class CourseListView(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated,WriteByAdminOnlyPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

