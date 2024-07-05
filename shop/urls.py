from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='index'),
    path('shopingcart/', views.shopingcart, name='shopingcart'),
    path('shopdetails/', views.shopdetails, name='shopdetails'),
]
 