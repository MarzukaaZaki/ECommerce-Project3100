from django.shortcuts import get_object_or_404, render
from products.models import Product
from categories.models import Category
from django.http import HttpResponse

# Create your views here.
def homePageView(response, category_slug = None):
    categories = None
    products = None
    if category_slug!=None:
        #return categories or show Error 404
        category_slug = get_object_or_404(Category,slug =category_slug)

        #return products or show Error 404
        products = Product.objects.filter(category=categories)
    else:
         products = Product.objects.all()
         categories = Category.objects.all()
         
    context  ={'products':products,'categories':categories}
    return render(response, 'home.html',context)


        
    
    
   