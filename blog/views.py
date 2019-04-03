from django.shortcuts import render,HttpResponse
from NiceBlog.settings import ROOT_URL
from blog.models import *
import json

def getAllBlog(request):
    if request.method == "GET":
        blog = BlogInfo.objects.all().values('id','author','title','content','imgurl',
        'classid','time','viewnum','commentnum','likenum')
        data = {}

        data['num'] = len(blog)
        for i in range(len(blog)):
            if blog[i]['imgurl'] == None:
                blog[i]['imgurl'] = "http://"+ROOT_URL+"/static/default.jpg"
            # if blog[i]['author'] == None or blog[i]['title'] == None or blog[i]['title'] == None
            data[i] = str(blog[i])

        return HttpResponse(json.dumps(data), content_type="application/json")

def getBlog(request):
    '''
    传入博客的id，到数据库中查询，获取博客信息
    :param request: id
    :return: 返回博客的标题和内容
    '''
    if request.method == "POST":
        blogid = request.POST.get('id',13)
        print(request.POST.get('id'))
        blog = BlogInfo.objects.filter(id=blogid).first()
        data = {}
        data['id'] = blogid
        data['title'] = blog.title
        data['content'] = blog.content
        data['imgUrl'] = blog.imgurl
        data['viewNum'] = blog.viewnum
        data['commentNum'] = blog.commentnum
        data['likeNum'] = blog.likenum
        data['author'] = blog.author
        data['time'] = str(blog.time)
        data['classid'] = blog.classid
        data['code'] = 0,
        data['message'] = "获取成功"
        return HttpResponse(json.dumps(data),content_type="application/json")