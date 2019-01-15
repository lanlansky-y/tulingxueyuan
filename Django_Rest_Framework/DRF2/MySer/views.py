from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from MySer.models import *
from MySer.serializers import *
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

# Create your views here.

class StudentVS(viewsets.ModelViewSet):
    pass


class StudentAPIView(APIView):
    '''
    处理用户的get请求
    '''
    def get(self, request):
        '''
        处理业务，跟数据库交互
        :param request:
        :return:
        '''

        stus = Student.objects.all()
        ser = StudentSerializer(stus)
        print(ser)
        return Response(data=ser.data)

class StudentGenAPIView(GenericAPIView):
    def get(self, request):
        print('haha')
        return None