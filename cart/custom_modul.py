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


class SendInfo:
    def __init__(self, pizza_list, total_cart_price, created_at):
        self.pizza_list = pizza_list
        self.total_cart_price = total_cart_price
        self.created_at = created_at


class ExceptionList(FileExistsError):
    pass
