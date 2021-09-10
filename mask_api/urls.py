from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('find_pharm_open_weekday_hour/', views.find_pharm_op_weekday_hour, name= 'find_pharmacies_open_weekday_hour'),
    path('find_pharm_sold_mask_sort/', views.find_pharm_sold_mask_sort, name= 'find_pharmacies_sold_mask_sort'),
    path('find_pharm_num_mask_price_range/', views.find_pharm_num_mask_price_range, name = 'find_pharm_num_mask_price_range'),
]

