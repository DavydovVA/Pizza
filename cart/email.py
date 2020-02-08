from django.core.mail import send_mail
from django.conf import settings


def build_message(his):
    name = his.user.get_full_name()
    plst = his.pizza_list
    total_price = his.total_cart_price

    string = f'Name: {name}\n\n{plst}\nTotal price: {total_price}$\n{his.address}'

    return string


def email(request, his):
    subject = 'Valera\'s Pizza'
    message = build_message(his)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]
    send_mail(subject, message, email_from, recipient_list)

    return True
