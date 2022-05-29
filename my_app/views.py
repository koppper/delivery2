from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm
from .models import Products, ProductCategory


def cart(request):
    return render(request, "my_app/cart.html")


def order(request):
    return render(request, "my_app/order.html")


# def main(request):
#     return render(request, "my_app/main.html")
#

# class Category(ListView):
#     model = ProductCategory
#     context_object_name = 'categories'
#     template_name = 'my_app/main.html'


def product_list(request, slug=None):
    category = None
    categories = ProductCategory.objects.all()
    products = Products.objects.filter(is_published=True)
    if slug:
        category = get_object_or_404(ProductCategory, slug=slug)
    products = products.filter(category=category)
    return render(request, 'my_app/main.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, pk, slug):
    product = get_object_or_404(Products, pk=pk, slug=slug, is_published=True)
    cart_product_form = CartAddProductForm()

    return render(request, 'my_app/product.html', {'product': product, 'cart_product_form': cart_product_form})



