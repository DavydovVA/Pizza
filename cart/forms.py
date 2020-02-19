from django import forms
from accounts.models import User
from django.core.exceptions import ValidationError


class PizzaForm(forms.Form):
    quantity = forms.CharField()
    quantity.widget = forms.TextInput(attrs={'class': 'form-control'})

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']

        chars = '0123456789'
        for i in quantity:
            if i not in chars:
                raise ValidationError('Price must contain only numeric characters.')

        if len(quantity) > 2:
            raise ValidationError('Too big quantity.')

        return quantity


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['phone_num', 'address']

        widgets = {
            'phone_num': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }