from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('find/<int:sid>', views.find),
    path('edit/', views.update),
]