from django.db import models
from categories.models import Category
from django.urls import reverse

# Create your models here.

# Product Model
class Product(models.Model):
    product_name = models.CharField(max_length= 40, unique= True)
    product_slug = models.SlugField(unique= True)
    product_desc = models.TextField()
    price        = models.DecimalField(max_digits= 7, decimal_places=3)
    product_img  = models.ImageField(upload_to = 'products') 
    category     = models.ForeignKey(Category,on_delete=models.CASCADE) # Deleting a category will automatically delete products of that category

    def __str__(self):
        return self.product_name

    # product url for single product view
    def get_product_url(self):
        return reverse('shop:product_detail',args=[self.category.slug,self.product_slug])
    