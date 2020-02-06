from django.urls import path

from cart import views

urlpatterns = [
    path('add/<int:product_id>/', views.AddToCart.as_view(), name='add_to_cart'),
    path('view/', views.ViewCart.as_view(), name='view_cart'),
]
