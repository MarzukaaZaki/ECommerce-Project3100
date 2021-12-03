from django.shortcuts import get_object_or_404, render
from products.models import Product
from categories.models import Category
from django.http import HttpResponse

# Create your views here.
def homePageView(response, category_slug = None):
    products = None
    # if the user clicks on a category
    if category_slug:
        #return categories or show Error 404
        categories = get_object_or_404(Category,slug =category_slug)

        #return products of the clicked category
        products = Product.objects.filter(category=categories)
    else:
        # else display all products
        products = Product.objects.all()

    # in both cases display all categories    
    categories = Category.objects.all()

    
    context  ={'categories':categories,'products':products,}
    return render(response, 'home.html',context)


        
    
    
   