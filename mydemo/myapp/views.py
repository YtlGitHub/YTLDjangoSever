from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse  # 导入反向解析地址
from myapp.models import Users
# Create your views here.


def index(request):
    print(reverse("add"))  # 通过路由名称反向生成url请求地址
    print(reverse("index"))
    print(reverse("find", args=(100, 'lisi')))
    print(reverse("edit"))
    print(reverse("fun", args=(2021, 12)))
    # return redirect(reverse("fun", args=(2021, 12)))  # 路由重定向
    return HttpResponse("Hello World!")


def add(request):
    return HttpResponse("add....")


def find(request, sid=0, name=""):
    return HttpResponse("find....%d:%s"%(sid, name))


def update(request):
    return HttpResponse("update....")
    # raise Http404("修改页面不存在!")


def fun(request, yy=1000, mm=10):
    return HttpResponse(f"参数信息：{yy}年{mm}月")


def index02(request):
    # 执行Model操作
    # # 添加操作
    # ob = Users()  # 实例化一个新对象，就是空对象
    # ob.name = '账上'
    # ob.age = 20
    # ob.sex = '男'
    # ob.classid = 'python06'
    # ob.save()  # 保存到数据库，新对象就是添加，已存在对象这是修改

    # # 删除操作
    # mod = Users.objects  # 获取Users的model对象
    # user = mod.get(id=8)  # 获取id值为6的数据信息
    # print(user.name)
    # user.delete()  # 执行删除操作

    # # 修改操作
    # ob = Users.objects.get(id=1)
    # print(ob.name)
    # ob.name = '张三'
    # ob.age = 26
    # ob.save()

    # 查询
    mod = Users.objects  # 获取Users模型的Model操作对象
    # ulist = mod.all()  # 获取所有数据
    # ulist = mod.filter(name='张三')  # 获取name值为张三的信息
    # ulist = mod.filter(age__gt=20)  # 获取所有age大于20岁的信息
    # ulist = mod.filter(age__gte=20)  # 获取所有age大于等于20岁的信息
    # ulist = mod.filter(age__lt=20)  # 获取所有age小于20岁的信息
    # ulist = mod.filter(age__lte=20)  # 获取所有age小于等于20岁的信息
    # ulist = mod.order_by("age")[:3]  # 按age升序排序,只获取前三条
    ulist = mod.raw('select * from stu where name="张三"')

    for u in ulist:
        print(u.id,u.name,u.age,u.sex,u.classid)

    return HttpResponse("成功")
