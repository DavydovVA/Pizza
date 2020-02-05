from accounts.forms import PizzaAuthenticationForm, PizzaUserCreationForm


def account_context(request):
    return {
        'login_form': PizzaAuthenticationForm(),
        'register_form': PizzaUserCreationForm()
    }
