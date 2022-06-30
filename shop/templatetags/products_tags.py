from django import template

from cart.forms import CartAddForm
from shop.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def cart_add_tags():
    return CartAddForm()
