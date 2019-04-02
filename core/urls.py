from django.urls import path
from . import views
from django.db import models
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('play/', views.play, name='play'),
]
