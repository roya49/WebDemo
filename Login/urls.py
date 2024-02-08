from django.urls import path
from . import views

urlpatterns = [
     path("", views.Login, name="index"),
     path('', views.index),
     path('', views.test),
]