"""url_shortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token

from api import views 

from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('urls/', include('core.urls')),
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token, name='rest-api-auth'),
    path('users/', views.UserList.as_view(), name='all-users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-details'),
    path('api-auth/', include('rest_framework.urls')),
]
