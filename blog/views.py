from django.shortcuts import render

# Create your views here.
#加载静态界面index首页s
def index(request):
    # request.META["CSRF_COOKIE_USED"] = True
    return render(request,'index.html')
