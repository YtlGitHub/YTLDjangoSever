from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('index02', views.index02, name='index02'),
    path('add/', views.add, name="add"),
    path('find/<int:sid>/<str:name>/', views.find, name="find"),
    path('edit/', views.update, name="edit"),
    re_path(r'^fun/(?P<yy>[0-9]{4})/(?P<mm>[0-9]{2})$', views.fun, name="fun"),
]