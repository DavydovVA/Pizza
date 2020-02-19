def create_info_for_history(cart):
    """creates a string to store history member"""
    string = ''
    for item in cart:
        title = item['product'].title
        price = float(item['product'].price)
        quan = int(item['quantity'])
        string += f"Pizza: {title}\nPrice: {price}$\nQuantity: {quan}\n\n"

    return string


class HistoryInfo:
    """is used to prepare info of history"""
    def __init__(self, pizza_list, total_cart_price, address, created_at):
        self.pizza_list = pizza_list
        self.total_cart_price = total_cart_price
        self.address = address
        self.created_at = created_at


class ExceptionList(FileExistsError):
    pass
