from django.urls import path
from django.urls.conf import include
from .views import homePageView
urlpatterns =[path('',homePageView,name ='home'),
path('<slug:category_slug>/', homePageView, name ='product_by_category')]