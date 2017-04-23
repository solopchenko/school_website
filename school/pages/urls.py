from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<page_url>[/\w-]*)/$', views.pages_detail, name='pages_detail'),
]
