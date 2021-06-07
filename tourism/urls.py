from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views




app_name = 'tourism'


urlpatterns =[
    path('all/',views.tourism_list,name='all-land'),
    path('filter/',views.filter,name='filter'),
    path('<str:slug>/<int:id>/',views.detail,name='product_detail'),
    path('<str:category_slug>/', views.show_tourism, name='product_list_by_show'),
]


