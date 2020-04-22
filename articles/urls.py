from django.urls import re_path,path
from . import views
app_name = 'articles'

urlpatterns = [
    re_path(r'create/', views.article_create, name='create'),
    re_path(r'(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
    path(r'', views.article_list, name='list'),
]