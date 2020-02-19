from django.core.mail import send_mail
from django.conf import settings
import socket


def build_message(his):
    """build message body"""
    name = his.user.get_full_name()
    p_list = his.pizza_list
    total_price = his.total_cart_price

    string = f'Name: {name}\n\n{p_list}\nTotal price: {total_price}$\n{his.address}'

    return string


def email(request, his):
    subject = 'Valera\'s Pizza'
    message = build_message(his)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email, ]

    # if no internet connection
    try:
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    except socket.gaierror:
        return False

    return True
