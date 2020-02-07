from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.views import View
from cart.cart import Cart
from pp.models import Pizza
from .forms import *
from .models import History


def create_info_for_history(cart):
    string = ''
    total_price = 0
    for item in cart:
        title = item['product'].title
        price = float(item['product'].price)
        quan = int(item['quantity'])
        string += f"Pizza: {title}\nPrice: {price}$\nQuantity: {quan}\n\n"
        total_price += price * quan

    return string, f'{total_price}$'


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


class AcceptOrder(View):
    @staticmethod
    def post(request):
        '''
        accepts changes in user
        and saves all order info in history
        '''
        form = UserForm(data=request.POST, instance=request.user)
        if form.is_valid():
            form.save()

        cart = Cart(request)
        pizza_list, total_price = create_info_for_history(cart)

        his = History(user=request.user, pizza_list=pizza_list, total_price=total_price)
        his.save()

        history_list = his.pizza_list.split('\n\n')[:-1]
        pizza_list = list()

        for item in history_list:
            pizza_list.append(item.split('\n'))

        cart.clear()

        return render(request, 'cart/checklist.html', context={'history': his, 'pizza_list': pizza_list})


class ViewOrder(View):
    @staticmethod
    def get(request):
        his = get_list_or_404(History, user=request.user)

        member_list = list()
        for member in his:
            pizza_list = list()
            tmp = member.pizza_list.split('\n\n')[:-1]
            for i in tmp:
                pizza_list.append(i.split('\n'))
            member_list.append(pizza_list)

        return render(request, 'cart/history.html', context={'member_list': member_list})



class ViewCart(View):
    @staticmethod
    def get(request):
        cart = Cart(request)
        user = request.user

        for item in cart:
            item['pizza_form'] = PizzaForm(initial={'quantity': item['quantity']})

        user_form = UserForm(initial={'phone_num': user.phone_num, 'address': user.address})

        return render(request, 'cart/view_cart.html', context={'cart': cart, 'user_form': user_form})


class RemoveFromCart(View):
    @staticmethod
    def post(request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Pizza, id=product_id)
        cart.remove(product)

        return redirect('cart:view_cart')
