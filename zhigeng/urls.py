"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from zhigeng import views,admin
from  django.conf.urls import include
from rest_framework import routers
# router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'zhigeng/list', views.Upload_list_, basename='Upload_list_')


urlpatterns = [
    # path('',views.home, name='home'),
    # path('list/', views.Upload_list_, name='Upload_list_'),
    path('add', views.add),
    path('upload_file', views.upload_file),
    path('update_topic_limits', views.update_topic_limits),
]
