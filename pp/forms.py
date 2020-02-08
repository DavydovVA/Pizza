from django import forms
from django.core.exceptions import ValidationError

from pp.models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['title', 'body', 'price', 'image']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'})
        }

    def clean_price(self):
        price = self.cleaned_data['price']

        chars = ',.0123456789'
        for i in price:
            if i not in chars:
                raise ValidationError('Price must contain only numeric characters.')

        if ',' in price:
            price = price.replace(',', '.')

        if '.' not in price:
            price += '.0'

        return price
