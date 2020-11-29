from django.contrib import admin
from .models import Product, Category
from orders.models import Order, OrderProducts


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_price')
    search_fields = ['name']
    list_filter = ('category__name',)

    def display_price(self, product):
        return f'PKR {product.price}'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    pass

@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    pass
