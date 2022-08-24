from django.urls import path
from . import views

urlpatterns = [

    path('orderitem/',views.orderItem , name="orderitem") , 




]