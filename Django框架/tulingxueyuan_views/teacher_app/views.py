from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def render_test(request):

    #环境变量
    c = dict()
    rsp = render(request, 'render.html')
    return rsp

def render2_test(request):

    #环境变量
    c = dict()
    c['name'] = 'TLXY'
    rsp = render(request, 'render2.html', context=c)
    return rsp

def render3_test(request):

    #得到模板
    from django.template import loader
    t = loader.get_template('render2.html')

    rsp = t.render(context={'name':'Tlxy'}, request=request)
    print(type(rsp))
    return HttpResponse(rsp)