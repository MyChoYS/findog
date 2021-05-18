"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from findog import views

urlpatterns = [
    path('', views.base, name='base'),
    path("main_board", views.main_board, name='main_board'),
    path('main_board_detail', views.main_board_detail, name='main_board_detail'),

    path('login', views.login, name='login'),
    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('login_register', views.login_register, name='login_register'),
    path('login_registerimpl', views.login_registerimpl, name='login_registerimpl'),
    path('logout', views.logout, name='logout'),
    path('androidlogin', views.androidlogin, name='androidlogin'),



]
