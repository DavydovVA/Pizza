from django.urls import path
from api import views


urlpatterns = [
    path('', views.PizzaApi.as_view()),
    path(r'users', views.UserApi.as_view())
]
