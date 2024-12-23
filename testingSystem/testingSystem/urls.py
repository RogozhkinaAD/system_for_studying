"""
URL configuration for testingSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import include, path
from core.views import indexPage, generatePassword

urlpatterns = [
    path('', indexPage),
    path('generatePassword', generatePassword),
    path("s/", include("core.urlsStudent")),
    path("staff/", include("core.urlsStaff")),
    path("personal/", include("core.urlsPersonal")),
    path("user/", include("userController.urls")),
    path('admin/', admin.site.urls),
]

