
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview,name="views"),
    path('tasklist/', views.tasklist, name="tasklist"),
    path('taskdetail/<int:pk>/', views.taskdetail, name="taskdetail"),
    path('taskcreate/', views.taskcreate, name="taskcreate"),
    path('taskupdate/<int:pk>', views.taskupdate, name="taskupdate"),
    path('taskdelete/<int:pk>', views.taskdelete,name="taskdelete")
]