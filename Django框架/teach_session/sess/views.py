from django.shortcuts import render
from sess.models import Student
from django.core.paginator import Paginator
from django.views.generic import ListView
# Create your views here.

def mySess(request):
    print(type(request.session))
    print(request.session)

    #如果session中没有teacher_name,则返回NoName
    print(request.session.get('teacher_name', 'NoName'))
    print('In mySess')
    return None

def student(request):
    '''
    请求所有学生的详情列表
    :param request:
    :return:
    '''
    #大约有10000名学生
    stus = Student.objects.all()

    #定义分页器，有两个参数：
    #1.数据来源，即从数据库中查询出的结果
    #2.单页返回数据量
    p = Paginator(stus, 40)
    #对Paginator进行设置或者使用其变量属性
    print(p.count)#p里面有多少数据
    print(p.num_pages)#页面总数


    return p

class StudentListView(ListView):
    '''
    需要设置两个主要内容
    1.queryset:数据来源集合
    2.template_name:模板名称
    '''
    queryset = Student.objects.all()

    template_name = ''