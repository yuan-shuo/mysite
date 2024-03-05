"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

# from app01 import views

# 这是array，数组间数据要用','分割
urlpatterns = [
    
    # """ polls """

    # path("polls/", include("polls.urls")),

    path("admin/", admin.site.urls),

    path("lea/", include("lea.urls")),

    # """ app01 """

    # www.xxx.com/index/ -> your function
    # path("index/", views.index),

    # path('userList/', views.userList),

    # path('tpl/', views.tpl),

    # path('redirect/', views.rdc),

    # path('orm/', views.orm),

    # # 用户登录案例
    # path('login/', views.login),

    # # 用户管理案例
    # path('info/show/', views.show),
    # path('info/get/', views.get),
    # path('info/delete/', views.delete),
]
