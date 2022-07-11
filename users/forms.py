from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from users.models import DeliveryAddress


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'autocomplete': 'email',
            'class': 'form-control input-text',
        })
    )
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control input-text'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control input-text'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control input-text'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control input-text'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control input-text'})


class AddDeliveryAddressForm(forms.ModelForm):

    class Meta:
        model = DeliveryAddress
        fields = ['country', 'city', 'street', 'house_number', 'apartment_number']
        widgets = {
        }

