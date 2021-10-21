from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse  # 导入反向解析地址
from myapp.models import Users
from datetime import datetime
from PIL import Image
import time
import os
# Create your views here.


# 首页
def index(request):
    # print(reverse("add"))  # 通过路由名称反向生成url请求地址
    print(reverse("index"))
    # print(reverse("find", args=(100, 'lisi')))
    # print(reverse("edit"))
    # print(reverse("fun", args=(2021, 12)))
    # return redirect(reverse("fun", args=(2021, 12)))  # 路由重定向
    # return HttpResponse("首页 <br> <a href='/users'>用户信息管理</a>")
    context = {}
    context['time'] = datetime.now
    return render(request, "myapp/index/index.html", context)


# 浏览用户信息
def index_users(request):
    try:
        ulist = Users.objects.all()
        context = {"userslist": ulist}
        return render(request, "myapp/users/index.html", context)  # 加载模板
    except:
        return HttpResponse("没有找到用户信息！")


# 浏览用户信息
def index_users2(request):
    #try:
        ulist = Users.objects.all()
        context = {"userslist": ulist}
        return render(request, "myapp/users/index2.html", context)  # 加载模板
    #except:
        #return HttpResponse("没有找到用户信息！")


# 加载添加用户信息
def add_users(request):
    return render(request, "myapp/users/add.html")


# 执行用户信息添加
def insert_users(request):
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
def del_users(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)  # 获取要删除的数据
        ob.delete()  # 执行删除操作
        context = {"info": "删除成功"}
    except:
        context = {"info": "删除失败"}
    return render(request, "myapp/users/info.html", context)


# 加载用户信息修改表单
def edit_users(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)  # 获取要修改的数据
        context = {"user": ob}
        return render(request, "myapp/users/edit.html", context)
    except:
        context = {"info": "没有找到要修改的数据!"}
        return render(request, "myapp/users/info.html", context)


# 执行用户信息修改
def update_users(request):
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


# 模板继承
def inherit(request):
    return render(request, "myapp/inherit/sub_template.html")


# 加载文件上传表单
def upload(request):
    return render(request, "myapp/upload/upload.html")


# 执行文件上传处理
def do_upload(request):
    myFile = request.FILES.get("pic", None)
    print(myFile)
    print(request.POST.get("title"))
    if not myFile:
        return HttpResponse("没有上传的文件信息")
    fileName = str(time.time())+'.'+myFile.name.split('.').pop()
    destination = open(f"./static/pics/{fileName}", "wb+")  # w读取b二进制，图片音频都属于二进制
    for chunk in myFile.chunks():  # 分块读取上传文件内容并写入目标文件
        destination.write(chunk)
    destination.close()  # 打开写入之后我们要关闭，用.close()这个方法关闭写入的文件
    # # 执行图片缩放
    # im = Image.open("./static/pics/"+fileName)
    # # 缩放到75*75(缩放后的宽高比例不变)
    # im.thumbnail((75, 75))
    # # 把缩放后的图像用jpeg格式保存
    # im.save("./static/pics/s_"+fileName, None)
    return HttpResponse("上传的文件："+fileName)
