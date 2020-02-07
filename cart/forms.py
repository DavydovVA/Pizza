from django import forms
from accounts.models import User


class PizzaForm(forms.Form):
    quantity = forms.CharField()
    quantity.widget = forms.TextInput(attrs={'class': 'form-control'})


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['phone_num', 'address']

        widgets = {
            'phone_num': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }