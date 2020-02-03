from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from pp.forms import PizzaForm
from pp.mixins import ListObjectsMixin
from pp.models import Pizza


class ListPizza(ListObjectsMixin, View):
    model = Pizza
    template_name = 'pp/index.html'
    template_include = 'pp/includes/pizz.html'


class ViewPizza(View):
    @staticmethod
    def get(request, slug):
        pizza = get_object_or_404(Pizza, slug=slug)

        return render(
            request,
            'pp/one_pizza.html',
            context={
                'pizza': pizza
            }
        )


class CreatePizza(LoginRequiredMixin, View):
    raise_exception = True

    @staticmethod
    def get(request):
        form = PizzaForm()

        return render(
            request,
            'pp/create_pizza.html',
            context={
                'form': form
            }
        )

    @staticmethod
    def post(request):
        form = PizzaForm(request.POST, request.FILES)

        if form.is_valid():
            pizza = form.save()
            pizza.save()

            return redirect(pizza)

        return render(
            request,
            'pp/create_pizza.html',
            context={
                'form': form
            }
        )