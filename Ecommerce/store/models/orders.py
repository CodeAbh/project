from django.db import models
from .product import Product
from .customor import Customer
import datetime


class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    prince = models.IntegerField()
    address = models.CharField(max_length=50, default='')
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)