from django.urls import path
from django.urls.conf import include
from .views import homePageView, productDetailView
app_name = 'shop'
urlpatterns =[path('',homePageView,name ='home'),
path('<slug:category_slug>/', homePageView, name ='product_by_category'),
path('<slug:category_slug>/<slug:product_slug>/', productDetailView, name ='product_detail'),

]