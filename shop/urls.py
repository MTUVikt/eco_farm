from django.urls import path

from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('category/<slug:category_slug>/', ProductCategoryListView.as_view(), name='category_product'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
]
