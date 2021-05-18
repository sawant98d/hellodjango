from testapp import views
from django.conf.urls import url

urlpatterns = [
    url('about', views.about),
    url('contact', views.showContact),
    url('^$', views.greeting),
    url('employee', views.employee_info_view)
]
