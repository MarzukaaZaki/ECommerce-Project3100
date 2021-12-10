from django.core import paginator
from django.shortcuts import get_object_or_404, render
from products.models import Product
from categories.models import Category
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import TemplateView

# Create your views here.
def homePageView(response, category_slug = None):
    products = None
    
    # if the user clicks on a category
    if category_slug:

        #return categories or show Error 404
        categories = get_object_or_404(Category,slug =category_slug)

        #return products of the clicked category
        products = Product.objects.filter(category=categories)
    
        # pagination of products
        p = Paginator(products,6)
    
    else:
    
        # else display all products
        products = Product.objects.all()
        
        # pagination of products
        p = Paginator(products,9)
    
    # in both cases display all categories    
    categories = Category.objects.all()
    
    # set the links to each page number 
    page_number = response.GET.get('page')
    paged_products = p.get_page(page_number)

    # context dictionary
    context  ={'categories':categories,'products':paged_products,}

    return render(response, 'home.html',context)



# product detail view
def productDetailView(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug,product_slug=product_slug)
    except Exception as e:
        raise e
    context = {'single_product':single_product}
    return render(request,'product_detail.html',context)        



    
   