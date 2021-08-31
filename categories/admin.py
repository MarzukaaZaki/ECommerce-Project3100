from django.contrib import admin
from .models import Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # generate slug automatically on entering category_name
    prepopulated_fields = {'slug' :('category_name',)}
    
    # display name & slug
    list_display = ('category_name','slug')

admin.site.register(Category,CategoryAdmin)
