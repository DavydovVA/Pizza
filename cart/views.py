from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from cart.cart import Cart
from pp.models import Pizza
from .forms import PizzaForm, UserForm


class AddToCart(View):
    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Pizza, id=product_id)
        cart.add(product=product)

        return redirect('cart:view_cart')


class ChangeQuan(View):
    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Pizza, id=product_id)
        form = PizzaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'])

        return redirect('cart:view_cart')


class ChangeUserInfo(View):
    @staticmethod
    def post(request):
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()

        return redirect('cart:view_cart')


class ViewCart(View):
    @staticmethod
    def get(request):
        cart = Cart(request)
        user = request.user

        for item in cart:
            item['pizza_form'] = PizzaForm(initial={'quantity': item['quantity']})

        user_form = UserForm(initial={'phone_num': user.phone_num, 'address': user.address})

        return render(request, 'cart/view_cart.html', context={'cart': cart, 'user_form': user_form})
