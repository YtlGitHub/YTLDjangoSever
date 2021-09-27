from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('users/', views.indexUsers, name='indexUsers'),
    path('users/add/', views.addUsers, name="addUsers"),
    path('users/insert/', views.insertUsers, name="insertUsers"),
    path('users/del/<int:sid>/', views.delUsers, name="delUser"),
    path('users/edit/<int:sid>/', views.editUsers, name="editUsers"),
    path('users/update/', views.updateUsers, name="updateUsers"),
]