from django.shortcuts import render,HttpResponse
from blog.models import *
import json

def getBlog(request):
    '''
    传入博客的id，到数据库中查询，获取博客信息
    :param request: id
    :return: 返回博客的标题和内容
    '''
    if request.method == "POST":
        blogid = request.POST.get('id',1)
        blog = Blog.objects.filter(id=blogid).first()
        data = {}
        data['id'] = blogid
        data['title'] = blog.title
        data['content'] = blog.content
        return HttpResponse(json.dumps(data),content_type="application/json")

