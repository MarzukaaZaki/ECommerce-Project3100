from django.forms import ModelForm
from .models import Category
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields =('category_name','slug','category_desc','category_img')