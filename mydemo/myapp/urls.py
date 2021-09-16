from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('find/<int:sid>/<str:name>/', views.find),
    path('edit/', views.update),
    re_path(r'^fun/(?P<yy>[0-9]{4})/(?P<mm>[0-9]{2})$', views.fun),
]