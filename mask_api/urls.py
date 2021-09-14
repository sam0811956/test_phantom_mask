from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('find_pharm_open_weekday_hour/', views.find_pharm_op_weekday_hour, name='find_pharm_open_weekday_hour'),
    path('find_pharm_sold_mask_sort/', views.find_pharm_sold_mask_sort, name='find_pharm_sold_mask_sort'),
    path('find_pharm_num_mask_price_range/', views.find_pharm_num_mask_price_range, name='find_pharm_num_mask_price_range'),
    path('find_user_date_range_top_total_amount/',views.find_user_date_range_top_total_amount, name='find_user_date_range_top_total_amount'),
    path('find_total_mask_num_dollar_date_range/', views.find_total_mask_num_dollar_date_range, name='find_total_mask_num_dollar_date_range'),
    path('search_pharm_mask_name/', views.search_pharm_mask_name, name='search_pharm_mask_name'),
    path('user_purchase_mask_atomic/', views.user_purchase_mask_atomic, name='user_purchase_mask_atomic'),
]

