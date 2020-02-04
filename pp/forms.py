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

    def clean_title(self):
        title = self.cleaned_data['title']

        if title.isdigit():
            raise ValidationError('Title must contain no numeric characters.')

        return title
