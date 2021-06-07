from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'blog'


urlpatterns =[
    path('news/',views.blog,name='guncel'),
    path('<str:slug>/',views.blog_detail,name='post_detail'),
]


