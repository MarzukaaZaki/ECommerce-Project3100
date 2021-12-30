from django.shortcuts import get_object_or_404, redirect, render
from .models import Product
from .forms import ProductForm
# Create your views here.
def productListView(request):
    all_products = Product.objects.all()
    context ={'all_products': all_products }
    return render(request, 'productindex.html',context)

def addProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('products:productlist')
    else:
        form = ProductForm()
        
    context_form ={'form':form}
    return render(request,'addproduct.html',context_form)

def productView(request,pk):
    product = get_object_or_404(Product,pk=pk)
    context = {'product':product}
    return render(request,'product.html',context)

def deleteProductView(request,pk):
    product = get_object_or_404(Product,pk=pk)
    product.delete()
    return redirect('products:productlist')

