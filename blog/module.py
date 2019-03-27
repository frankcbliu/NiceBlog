'''
该文件是为了方便管理 module 多页面，可理解为从 views.py 中分离出一部分来
'''
from django.shortcuts import render

# Create your views here.
#加载静态界面index首页s
def index(request):
    return render(request,'index.html')

def moduleIndex(request):
    return render(request,'blog/index.html')

def moduleDetail(request):
    return render(request,'blog/detail.html')