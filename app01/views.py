from django.shortcuts import render
from .models import *
from django.http import *

# Create your views here.

# 定义首页
def gotoIndex(request):
    return render(request, "index.html")

# 去注册页面
def gotoregister(request):
    return render(request, "register.html")

# 注册，将信息存到数据库
def register(request):
    uname = request.POST.get("uname")
    upwd = request.POST.get("upwd")
    user = User(uname=uname, upwd=upwd)
    user.save()
    return render(request, "index.html")

# 去登录页面
def gotologin(request):
    return render(request, "login.html")

# 登录，验证是够有该用户并且密码是否正确
def login(request):
    uname = request.POST.get("uname")
    upwd = request.POST.get("upwd")
    user = User.objects.get(uname=uname)
    if user:
        if user.upwd==upwd:
            # 添加session
            dic = {}
            dic["uname"] = uname
            request.session["user"] = dic
            return render(request, "gotogoods.html", dic)
        return HttpResponse("密码错误")
    return HttpResponse("没有该用户")

# 查看商品
def goods(request):
    goodslist = Goods.objects.all()
    dic = request.session.get("user")
    dic["goodslist"] = goodslist
    return render(request, "goods.html", dic)

# 转到添加商品页面
def gotoaddgoods(request):
    dic = request.session.get("user")
    return render(request, "addgoods.html", dic)

# 添加商品到数据库
def addgoods(request):
    gname = request.POST.get("gname")
    g = Goods(gname=gname)
    g.save()
    dic = request.session.get("user")
    return render(request, "gotogoods.html", dic)

# 删除商品
def delgoods(request):
    gid = request.GET.get("gid")
    Goods.objects.filter(gid=gid).delete()
    dic = request.session.get("user")
    return render(request, "gotogoods.html", dic)

# 修改商品
def editgoods(request):
    gid = request.GET.get("gid")
    g = Goods.objects.get(gid=gid)
    dic = request.session.get("user")
    dic["goods"] = g
    return render(request, "editgoods.html", dic)

# 更新商品
def updategoods(request):
    gid = request.POST.get("gid")
    g = Goods.objects.get(gid=gid)
    g.gname = request.POST.get("gname")
    g.save()
    dic = request.session.get("user")
    return render(request, "gotogoods.html", dic)