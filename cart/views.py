from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from cart.cart import Cart
from pp.models import Pizza
from django.views.decorators.http import require_POST


class AddToCart(View):
    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Pizza, id=product_id)
        cart.add(product=product)

        return render(request, 'cart/view_cart.html', context={'cart': cart})


class ViewCart(View):
    @staticmethod
    def get(request):
        cart = Cart(request)
        current_user = request.user

        return render(request, 'cart/view_cart.html', context={'cart': cart, 'user': current_user})
