from django.core.mail.backends import console
from django.shortcuts import render, redirect
from .forms import ProductForm, ProductOptionForm
from .models import *


# Create your views here.
# First 3 api's are performed here\
# 1. `GET /products` - gets all products
# 2. `GET /products?name={name}` - finds all products matching the specified name.
# 3. `GET /products/{id}` - gets the project that matches the specified ID
def product_list(request):
    if 'query_text' in request.GET:
        query_text = request.GET['query_text']
        # as the search bar allows to search by id and name checking the type of query_text before sending to db query
        if query_text.isnumeric():
            context = {'product_list': Product.objects.filter(id__exact=query_text).order_by('product_name')}
        if isinstance(query_text, str):
            context = {
                'product_list': Product.objects.filter(product_name__icontains=query_text).order_by('product_name')}
    # if listing of all products is required fetching of all records is done here
    else:
        context = {'product_list': Product.objects.all().order_by('product_name')}

    return render(request, "product_register/product_list.html", context);


# both creating and updating products are done here
def product_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(instance=product)
        return render(request, "product_register/product_form.html", {'form': form});
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            product = Product.objects.get(pk=id)
            form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("/product/list")


# deleting product based on id passed
def product_delete(request, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return redirect("/product/list")


# helps to search product options based on product name
def product_option_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        context = {'product_option_list': ProductOption.objects.filter(Product__product_name__icontains=q).order_by(
            'Product__product_name')}
    else:
        context = {'product_option_list': ProductOption.objects.all().order_by('Product__product_name')}

    return render(request, "product_register/product_option_list.html", context);


# helps to create new product option and also update product option to fit new products

def product_option_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProductOptionForm()
        else:
            product_option = ProductOption.objects.get(pk=id)
            form = ProductOptionForm(instance=product_option)
        return render(request, "product_register/product_option_form.html", {'form': form});
    else:
        if id == 0:
            form = ProductOptionForm(request.POST)
        else:
            product_option = ProductOption.objects.get(pk=id)
            form = ProductOptionForm(request.POST, instance=product_option)
        if form.is_valid():
            form.save()
        return redirect("/product/product_option_list")


# delete corresponding product option and maintains product linked
def product_option_delete(request, id):
    product_option = ProductOption.objects.get(pk=id)
    product_option.delete()
    return redirect("/product/product_option_list")


# handles unspecified roots
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)
