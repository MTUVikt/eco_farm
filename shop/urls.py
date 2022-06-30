from django.urls import path

from .views import *

urlpatterns = [
    path('', product_list, name='product_list'),
    path('category/<slug:category_slug>/', get_category, name='category_product'),
    path('<slug:slug>/', product_detail, name='product_detail'),
]
