from django.contrib import admin
from .models import Product, Category, StockMovement, Supplier, Warehouse

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(StockMovement)
admin.site.register(Supplier)
admin.site.register(Warehouse)
