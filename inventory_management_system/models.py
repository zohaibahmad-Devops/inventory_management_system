from django.db import models


class InputProduct(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    price_in = models.IntegerField(default=0, blank=True, null=True)
    price_out = models.IntegerField(default=0, blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.item_name


class Expenses(models.Model):
    rent = models.IntegerField(default='0', blank=True, null=True)
    gas_bill = models.IntegerField(default='0', blank=True, null=True)
    electricity_bill = models.IntegerField(default='0', blank=True, null=True)
    maintenance = models.IntegerField(default='0', blank=True, null=True)
    staff_salaries = models.IntegerField(default='0', blank=True, null=True)


class Customer(models.Model):
    identity = models.IntegerField(primary_key=True)
    customer_name = models.CharField(max_length=50, blank=True, null=True)

    # balance = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.customer_name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    success = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    product = models.ForeignKey(InputProduct, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)


class Bill(models.Model):
    identity = models.ForeignKey(Customer, on_delete=models.CASCADE)
