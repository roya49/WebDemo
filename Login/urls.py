from django.urls import path
from . import views

urlpatterns = [
     path("", views.login, name="index"),
     path('index/', views.index),
     path('test/', views.test),
]
