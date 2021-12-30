from django.db import models
from products.models import Product
from django.contrib import admin

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # specify attributes to display 
    list_display        = ('product_name','price',)
    # Add a filter that can be used to filter products by category
    list_filter = ('category',)
    
    # Adds a search box 
    search_fields = ('product_name__startswith',)
    
    # Generates slug based on product name
    prepopulated_fields = {'product_slug':('product_name',)}

# Register Product model and ProductAdmin    
admin.site.register(Product,ProductAdmin)