
from django.forms import ModelForm
from .models import Product
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields =('product_name','product_desc','price','category')
