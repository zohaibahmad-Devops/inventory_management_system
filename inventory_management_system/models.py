from django.db import models


class InputProduct(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    price_in = models.IntegerField(default=0, blank=True, null=True)
    price_out = models.IntegerField(default=0, blank=True, null=True)
    last_update = models.DateTimeField(auto_now_add=False, auto_now=True)
