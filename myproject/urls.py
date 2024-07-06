"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome),
    path('login/',views.login),
    path('register/',views.register),
    path('myadmin/',views.admin),
    path('myhr/',views.hr),
    path('allUserData/',views.allUser),
    path('changeStatus/<int:UserId>/',views.changeStatus),
    path('deleteUser/<int:UserId>/',views.deleteUser),
    path('editUser/<int:UserId>/',views.editUser),
    path('logout/',views.logout),
    path('editProfile/<int:UserId>/',views.editProfile),
    path('allEmployeeData/',views.allEmployeeData),
    path('applyLeave/',views.applyLeave),
    path('employeelanding/',views.employeelanding)
] 
