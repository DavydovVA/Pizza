from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404, Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from cart.cart import Cart, get_cart_len
from pp.models import Pizza
from .models import History
from .forms import *
from .custom_modul import *
from .email import email


class AddToCartView(View):
    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Pizza, id=product_id)
        cart.add(product=product)

        return redirect('cart:view_cart')


class ChangeQuantityView(View):
    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Pizza, id=product_id)
        form = PizzaForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'])

        return redirect('cart:view_cart')


class AcceptOrderView(View):
    @staticmethod
    def post(request):
        form = UserForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()

        cart = Cart(request)
        pizza_list = create_info_for_history(cart)
        total_cart_price = cart.get_total_cart_price()

        his = History(user=request.user,
                      pizza_list=pizza_list,
                      address=request.user.address,
                      total_cart_price=total_cart_price
                      )

        history_list = his.pizza_list.split('\n\n')[:-1]
        pizza_list = list()

        for item in history_list:
            pizza_list.append(item.split('\n'))

        total_cart_price = cart.get_total_cart_price()

        if not email(request, his):
            return redirect('cart:view_cart')

        his.save()
        cart.clear()

        return render(request, 'cart/checklist.html',
                      context={'history': his,
                               'pizza_list': pizza_list,
                               'total_cart_price': total_cart_price}
                      )


class GetHistoryView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        try:
            his = get_list_or_404(History.objects.all().order_by('-created_at'), user=request.user)
        except Http404:
            his = list()

        member_list = list()

        if his:
            """if history is not empty, collect and prepare history members"""
            for member in his:
                pizza_list = list()
                tmp = member.pizza_list.split('\n\n')[:-1]  # -1, because last member is ''
                for i in tmp:
                    pizza_list.append(i.split('\n'))

                member_list.append(HistoryInfo(
                            pizza_list,
                            member.total_cart_price,
                            member.address,
                            member.created_at
                        ))

            return render(request, 'cart/history.html',
                          context={'member_list': member_list,
                                   'cart_len': get_cart_len(request)
                                   }
                          )

        return render(request,
                      'cart/history.html',
                      context={'member_list': False,
                               'cart_len': get_cart_len(request)
                               }
                      )


class GetCartView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        cart = Cart(request)
        user = request.user

        for item in cart:
            item['pizza_form'] = PizzaForm(initial={'quantity': item['quantity']})

        user_form = UserForm(initial={'phone_num': user.phone_num, 'address': user.address})

        return render(request,
                      'cart/view_cart.html',
                      context={'cart': cart,
                               'user_form': user_form,
                               'cart_len': get_cart_len(request)
                               }
                      )


class RemoveFromCartView(View):
    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Pizza, id=product_id)
        cart.remove(product)

        return redirect('cart:view_cart')
