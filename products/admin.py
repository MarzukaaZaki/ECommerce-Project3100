from django.db import models
from products.models import Product
from django.contrib import admin

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display        = ('product_name','category','price')
    prepopulated_fields = {'product_slug':('product_name',)}
admin.site.register(Product,ProductAdmin)