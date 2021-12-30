from django.shortcuts import get_object_or_404, redirect, render
from categories.forms import CategoryForm
from categories.models import Category

# Lists all the categories
def categoryListView(request):
    
    # Fetches all categories to display in the template 
    all_categories = Category.objects.all()
    
    # Passes the instance in a dictionary
    context ={'all_categories': all_categories }
    
    return render(request, 'index.html',context)

# Adds a new category
def addCategory(request):

    # If form wants to send data via POST request
    if request.method == 'POST':
        
        # Allows user to fill in the form
        form = CategoryForm(request.POST)

        # Checks if data entered is correct
        if form.is_valid():
            # Saves the data entered in the form
            category = form.save(commit=False)
            # Saves the data in the database permanently
            category.save()
            return redirect('categories:list')

    # Else create a blank form
    else:
        # Uses the fields in CategoryForm class to create it
        form = CategoryForm()

    # Passes the instance in a dictionary    
    context_form ={'form':form}
    return render(request,'addcategory.html',context_form)



# Displays details of a category
def categoryDetailView(request,pk):
    
    # Retrieves particular object based on primary key 
    category = get_object_or_404(Category,pk=pk)
    
    # Passes the instance in a dictionary 
    context = {'category':category}
    return render(request,'category_detail.html',context)


# Deletes a category
def deleteCategoryView(request,pk):

    # Retrieves particular object based on primary key 
    category = get_object_or_404(Category,pk=pk)
    
    # Deletes the particular object from its model
    category.delete()
    return redirect('categories:list')
