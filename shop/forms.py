from django import forms

from .models import CartItem


class AddToCart(forms.Form):
    quantity = forms.IntegerField()
