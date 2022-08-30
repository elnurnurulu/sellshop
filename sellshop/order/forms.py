
from order.models import BillingAddress,ShippingAddress
from django import forms
from django.forms import widgets

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = ('user',)
        fields = [
            'user',
            'first_name',
            'last_name',
            'address',
            'city',
            'zipcode',
            'country',
            
            'phone',
 ]

        widgets = {
            'user': widgets.Select(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'last_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'address': widgets.TextInput(attrs={'class': 'input-text'}),
            'city': widgets.TextInput(attrs={'class': 'input-text'}),
            'zipcode': widgets.TextInput(attrs={'class': 'input-text'}),
            'phone': widgets.TextInput(attrs={'class': 'input-text'}),
        }



class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = [
            'user',
            'first_name',
            'last_name',
            'address',
            'city',
            'zipcode',
            'country',
            'phone',]

        widgets = {
            'user' : widgets.Select(attrs={'class': 'form-control'}),
            'first_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'last_name': widgets.TextInput(attrs={'class': 'input-text'}),
            'address': widgets.TextInput(attrs={'class': 'input-text'}),
            'city': widgets.TextInput(attrs={'class': 'input-text'}),
            'zipcode': widgets.TextInput(attrs={'class': 'input-text'}),
            'phone': widgets.TextInput(attrs={'class': 'input-text'}),
        }