from django.contrib import admin

from products.models import Product
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # generate slug automatically on entering category_name
    prepopulated_fields = {'slug' :('category_name',)}
    
    # specify the attributes to display 
    list_display = ('category_name','no_of_products','category_desc',)
    search_fields = ('category_name__startswith',)

    # display info using query expressions
    def no_of_products(self,obj):
        from django.db.models import Count
        total = Product.objects.filter(category=obj).aggregate(Count("product_name"))
        return total["product_name__count"]

admin.site.register(Category,CategoryAdmin)
