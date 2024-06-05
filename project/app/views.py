from django.shortcuts import render
from .models import Teacher,Student,Clas
from rest_framework import viewsets
from .serializers import StudentSerializerClass,ClasSerializerClass,TeacherSerializerClass
# Create your views here.



class ClasAPIViewSet(viewsets.ModelViewSet):
    queryset = Clas.objects.all()
    serializer_class = ClasSerializerClass



class TeacherAPIViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializerClass


class StudentAPIViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializerClass
