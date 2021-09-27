from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse  # 导入反向解析地址
from myapp.models import Users
from datetime import datetime
# Create your views here.


def index(request):
    # print(reverse("add"))  # 通过路由名称反向生成url请求地址
    print(reverse("index"))
    # print(reverse("find", args=(100, 'lisi')))
    # print(reverse("edit"))
    # print(reverse("fun", args=(2021, 12)))
    # return redirect(reverse("fun", args=(2021, 12)))  # 路由重定向
    return HttpResponse("首页 <br> <a href='/users'>用户信息管理</a>")


# 浏览用户信息
def indexUsers(request):
    #try:
        ulist = Users.objects.all()
        context = {"userslist": ulist}
        return render(request, "myapp/users/index.html", context)  # 加载模板
    #except:
        #return HttpResponse("没有找到用户信息！")


# 加载添加用户信息
def addUsers(request):
    return render(request, "myapp/users/add.html")


# 执行用户信息添加
def insertUsers(request):
    try:
        ob = Users()
        # 从表单中获取要添加的信息并封装到ob对象里面
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.sex = request.POST['sex']
        ob.classid = request.POST['classid']
        ob.save()  # 执行保存
        context = {"info": "添加成功"}
    except:
        context = {"info": "添加失败"}
    return render(request, "myapp/users/info.html", context)


# 执行用户信息删除
def delUsers(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)  # 获取要删除的数据
        ob.delete()  # 执行删除操作
        context = {"info": "删除成功"}
    except:
        context = {"info": "删除失败"}
    return render(request, "myapp/users/info.html", context)


# 加载用户信息修改表单
def editUsers(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)  # 获取要修改的数据
        context = {"user": ob}
        return render(request, "myapp/users/edit.html", context)
    except:
        context = {"info": "没有找到要修改的数据!"}
        return render(request, "myapp/users/info.html", context)


# 执行用户信息修改
def updateUsers(request):
    try:
        uid = request.POST['id']  # 获取要修改书记的id号
        ob = Users.objects.get(id=uid)  # 查询要修改的数据
        # 从表单中获取要修改的信息并封装到ob对象里面
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.sex = request.POST['sex']
        ob.classid = request.POST['classid']
        ob.addtime = datetime.now()
        ob.save()  # 执行保存
        context = {"info": "修改成功"}
    except:
        context = {"info": "修改失败"}
    return render(request, "myapp/users/info.html", context)
