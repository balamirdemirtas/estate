from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'real'


urlpatterns =[
    path('',views.index,name ='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('team/',views.team,name='team'),
    path('document/',views.documents,name='document'),
    path('<str:slug>/<int:id>/',views.detail,name='product_detail'),
    path('<str:category_slug>/', views.show, name='product_list_by_show'),

]


