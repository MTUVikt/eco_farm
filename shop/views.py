
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from cart.forms import CartAddForm
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(aviable=True)


class ProductCategoryListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['category_slug'], aviable=True)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, aviable=True)
#     cart_add_form = CartAddForm
#     context = {
#         'product': product,
#         'cart_add_form': cart_add_form,
#     }
#     return render(request, 'shop/product_detail.html', context)

# class ProductDetailView(DetailView):
#     model = Product
