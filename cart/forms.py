from django import forms
from accounts.models import User


class PizzaForm(forms.Form):
    quantity = forms.CharField()


class UserForm(forms.ModelForm):
    class Meta:
        model = User

        fields = ['phone_num', 'address']
