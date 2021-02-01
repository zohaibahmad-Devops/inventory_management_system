from django.contrib import admin

from inventory_management_system.models import InputProduct, Expenses, OrderItem, Order, Customer

admin.site.register(InputProduct)
admin.site.register(Expenses)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

admin.site.site_header = 'Admin Site for Inventory System developed by Zohaib Ahmad'
