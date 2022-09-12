from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<id>\d+)$', views.newsDetailview, name='news_detail'),
    re_path(r'^workers/$', views.workersList.as_view(), name = 'worker_list'),
    re_path(r'^product/$', views.ProductList, name="poezda"),

]
