"""hellodjango URL Configuration

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
from django import urls
from django.contrib import admin
from django.urls import path
from testapp import views as testapp_views
from exam import views as exam_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', testapp_views.greeting),
    path('about/', testapp_views.about),
    path('contact/',testapp_views.showContact),
    #url('^$', views.greeting)    
    path('', testapp_views.greeting),#same as above

    path('test/', exam_views.showTest),
    path('result/', exam_views.showResult)
]
