from django.urls import path

from pp import views

urlpatterns = [
    path('', views.ListPizza.as_view(), name='index'),
    path('create/', views.CreatePizza.as_view(), name='create_pizza'),
    path('<slug:slug>/', views.ViewPizza.as_view(), name='pizza'),
]
