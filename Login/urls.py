from django.urls import path
from Login import views

urlpatterns = [
     path("", views.Login.as_view(), name="index")

]