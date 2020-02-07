from pp.models import Pizza as Product
from Pizza import settings


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        self._status = True

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
            self._status = False
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=True):
        product_id = str(product.id)

        self._status = True

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = item['product'].price
            item['total_price'] = float(item['product'].price) * float(item['quantity'])
            item['image'] = item['product'].image
            yield item

    def __bool__(self):
        return self._status


    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True


