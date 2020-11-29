from django.db import models

from catalogue.models import Product


class Order(models.Model):
    customer_id = models.IntegerField(default=1)
    status = models.IntegerField(default=None)
    products = models.ManyToManyField(Product, through='OrderProducts')


class OrderProducts(models.Model):
    order = models.ForeignKey(Order, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField(default=0.00)

    class Meta:
        db_table = 'orders_order_products'
        unique_together = (('order', 'product'),)
        verbose_name_plural = 'OrderProducts'
