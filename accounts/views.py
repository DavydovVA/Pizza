from django.contrib.auth.views import LoginView
from django.shortcuts import reverse
from django.views.generic import FormView

from accounts.forms import PizzaAuthenticationForm, PizzaUserCreationForm
from accounts.mixins import AccountModalMixin


class PizzaLoginView(AccountModalMixin, LoginView):
    form_name = 'login'
    error_message = 'Invalid username or password'
    form_class = PizzaAuthenticationForm


class PizzaUserCreationView(AccountModalMixin, FormView):
    form_name = 'register'
    form_class = PizzaUserCreationForm

    def form_valid(self, form):
        form.save()

        path = self.request.GET.get('next', reverse('pp:index'))
        self.success_url = f'{path}?form={PizzaLoginView.form_name}'

        return super().form_valid(form)
