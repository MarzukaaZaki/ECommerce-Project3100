from categories.views import addCategory, categoryListView


from django.urls import path
from . import views
app_name = 'categories'
urlpatterns = [
    path('',views.categoryListView,name ='list'),
    path('add/',views.addCategory, name ='add'),
    path('details/<int:pk>',views.categoryDetailView, name = 'details'),
    path('delete/<int:pk>',views.deleteCategoryView,name ='delete'),
]
