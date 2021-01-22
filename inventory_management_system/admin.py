from django.contrib import admin
from .forms import StockCreateForm
from .models import Stock


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity', 'issue_by']
    form = StockCreateForm
    list_filter = ['category','item_name']
    search_fields = ['category', 'item_name']


admin.site.register(Stock, StockCreateAdmin)