from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('app02', views.app02, name='app02'),
]
