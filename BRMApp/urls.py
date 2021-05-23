from BRMApp import views
from django.conf.urls import url

urlpatterns = [
    url('view-books', views.viewBooks)    
]