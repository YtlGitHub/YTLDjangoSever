from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),  # 首页
    path('users/', views.index_users, name='indexUsers'),  # 浏览用户信息
    path('users2/', views.index_users2, name='indexUsers2'),  # 浏览用户信息
    path('users/add/', views.add_users, name="addUsers"),  # 加载添加用户信息
    path('users/insert/', views.insert_users, name="insertUsers"),  # 执行用户信息添加
    path('users/del/<int:uid>/', views.del_users, name="delUsers"),  # 执行用户信息删除
    path('users/edit/<int:uid>/', views.edit_users, name="editUsers"),  # 加载用户信息修改表单
    path('users/update/', views.update_users, name="updateUsers"),  # 执行用户信息修改
    path('inherit/', views.inherit, name="inherit"),  # 模板继承
    path('upload/', views.upload, name="upload"),  # 加载文件上传表单
    path('doUpload/', views.do_upload, name="doUpload"),  # 执行文件上传处理
]