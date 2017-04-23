from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.staff_list, name='staff_list'),
    url(r'^(?P<username>[\w-]+)/$', views.staff_detail, name='staff_detail'),
]
