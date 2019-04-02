from django.urls import path
from . import views
from django.db import models
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('deck/<slug:slug>/create/', views.create_card, name='create_card'),
]
