from categories.models import Category
from django.db import models

# Create your models here.

# Product Model
class Product(models.Model):
    product_name = models.CharField(max_length= 40, unique= True)
    product_slug = models.SlugField(unique= True)
    product_desc = models.TextField()
    price        = models.DecimalField(max_digits= 7, decimal_places=3)
    product_img  = models.ImageField(upload_to = 'media/product_images') 
    category     = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
    