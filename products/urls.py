from django.urls import path
from . import views
app_name = 'products'
urlpatterns = [
    path('',views.productListView,name ='productlist'),
    path('addproduct/',views.addProduct, name ='addproduct'),
    path('productdetails/<int:pk>',views.productView, name = 'productdetails'),
    path('deleteproduct/<int:pk>',views.deleteProductView,name ='deleteproduct'),
]
