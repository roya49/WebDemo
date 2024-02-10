from django.urls import path
from . import views

urlpatterns = [
     path("", views.login, name="index"),
     path('stuff/', views.stuff),
     path('stuff_list/', views.stuffList),
     path('index/', views.index),
     path('test/', views.test),
     path('work/', views.work),
     path('add/', views.add)
]