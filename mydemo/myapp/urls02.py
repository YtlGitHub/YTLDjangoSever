from django.urls import path, re_path
from . import views02


urlpatterns = [
    path('', views02.index, name="index"),
    path('index02', views02.index02, name='index02'),
    path('add/', views02.add, name="add"),
    path('find/<int:sid>/<str:name>/', views02.find, name="find"),
    path('edit/', views02.update, name="edit"),
    re_path(r'^fun/(?P<yy>[0-9]{4})/(?P<mm>[0-9]{2})$', views02.fun, name="fun"),
]