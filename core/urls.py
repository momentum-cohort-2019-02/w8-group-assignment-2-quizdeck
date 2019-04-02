from django.urls import path
from . import views
from django.db import models
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('play/', views.play, name='play'),
    path('deck_detail/<slug:slug>', views.deck_detail, name='deck_detail'),
    path('deck/<slug:slug>/create/', views.create_card, name='create_card'),

]
