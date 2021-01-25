from django.contrib import admin

from inventory_management_system.models import InputProduct

admin.site.register(InputProduct)

admin.site.site_header = 'inventory_management_system Admin'
