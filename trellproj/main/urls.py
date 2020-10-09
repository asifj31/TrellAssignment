from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('signup/', views.signupuser, name='signupuser' ),
    path('logout/', views.logoutuser, name='logoutuser' ),
    path('login/', views.loginuser, name='loginuser' ),
    path('main/', views.mainpage, name='mainpage' ),
    path('addmovies/', views.addmovies, name='addmovies' ),
]
