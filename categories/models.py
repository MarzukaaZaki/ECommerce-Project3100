from django.db import models
from django.urls import reverse

# Category model
class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length = 100,unique=True)
    category_desc = models.TextField()
    category_img = models.ImageField(upload_to = 'categories', null = True)
    
    # Metadata
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    # Methods

    # shows the name of category 
    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('shop:product_by_category',args=[self.slug])



