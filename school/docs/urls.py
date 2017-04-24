from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.docs_list, name='docs_list'),
]
