"""ZemoSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from pages.views import contact_view, about_view
from guild.views import home_view, guild_view
from commands.views import commands_view
from django.contrib.auth.views import LoginView
from commands.views import add_command_view, delete_command_view, add_admin_command_view, delete_admin_command_view
from error.views import error_400

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('admin/', admin.site.urls, name='admin'),
    path('commands/', commands_view),
    path('login/', LoginView.as_view(), name='login'),
    path('guild/', guild_view, name='guild'),
    path('commands/add-command/', add_command_view, name='add_command'),
    path('commands/delete-command/', delete_command_view, name='delete_command'),
    path('commands/add-admin-command/', add_admin_command_view, name='add_admin_command'),
    path('commands/delete-admin-command/', delete_admin_command_view, name='delete_admin_command'),
    path('400/', error_400, name='error_400')
]