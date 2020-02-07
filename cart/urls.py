from django.urls import path

from cart import views

urlpatterns = [
    path('add/<int:product_id>/', views.AddToCart.as_view(), name='add_to_cart'),
    path('cart/', views.ViewCart.as_view(), name='view_cart'),
    path('update/<int:product_id>', views.ChangeQuan.as_view(), name='update_quan'),
    path('accept_order/', views.AcceptOrder.as_view(), name='accept_order'),
    path('order/', views.ViewOrder.as_view(), name='order'),
    path('remove/<int:product_id>', views.RemoveFromCart.as_view(), name='remove'),
]
