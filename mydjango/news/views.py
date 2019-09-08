from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'baidu.html')

def login(request):
    return HttpResponse('<h1>{}<h1>'.format(request.path))

# 404页面的配置
def page_not_found(request):
    return render(request,'404.html')