
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from cart.forms import CartAddForm
from .models import Product


def product_list(request):
    products = Product.objects.filter(aviable=True)
    context = {
        'products': products,
    }
    return render(request, 'shop/product_list.html', context)


def get_category(request, category_slug):
    products = Product.objects.filter(category__slug=category_slug, aviable=True)
    context = {
        'products': products,
    }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, aviable=True)
    cart_add_form = CartAddForm
    context = {
        'product': product,
        'cart_add_form': cart_add_form,
    }
    return render(request, 'shop/product_detail.html', context)

# class ProductDetailView(DetailView):
#     model = Product
