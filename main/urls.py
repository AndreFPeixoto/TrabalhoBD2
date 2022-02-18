"""CMSocial URL Configuration

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
from django.contrib import admin
from django.urls import path
from app.views import welcome, enter, create_account, exit, home, create_user, read_user, update_user, delete_user, create_group, read_group, update_group, delete_group

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome, name='url_welcome'),
    path('enter/', enter, name='url_enter'),
    path('create_account/', create_account, name='url_create_account'),
    path('', home, name='url_home'),
    path('exit/', exit, name='url_exit'),
    path('create_user/', create_user, name='url_create_user'),
    path('read_user/', read_user, name='url_read_user'),
    path('update_user/<int:pk>/', update_user, name='url_update_user'),
    path('delete_user/<int:pk>/', delete_user, name='url_delete_user'),
    path('create_group/', create_group, name='url_create_group'),
    path('read_group/', read_group, name='url_read_group'),
    path('update_group/<int:pk>/', update_group, name='url_update_group'),
    path('delete_group/<int:pk>/', delete_group, name='url_delete_group'),
]
