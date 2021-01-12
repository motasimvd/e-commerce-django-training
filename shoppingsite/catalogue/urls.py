from django.urls import path

from .views import home, product_list_view, product_create_view, product_delete_view, product_update_view, \
    category_list_view

urlpatterns = [
    path('', home, name='home-view'),
    path('products/', product_list_view, name='product-list'),
    path('products/create', product_create_view, name='product-create'),
    path('product/<int:product_id>/delete', product_delete_view, name='product-delete'),
    path('product/<int:product_id>/update', product_update_view, name='product-update'),
    path('categories/', category_list_view, name='category-list')
]
