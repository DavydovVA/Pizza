from django.urls import path

from cart import views

urlpatterns = [
    path('add/<int:product_id>/', views.AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', views.GetCartView.as_view(), name='view_cart'),
    path('update/<int:product_id>', views.ChangeQuantityView.as_view(), name='update_quantity'),
    path('check/', views.AcceptOrderView.as_view(), name='accept_order'),
    path('history/', views.GetHistoryView.as_view(), name='order'),
    path('remove/<int:product_id>', views.RemoveFromCartView.as_view(), name='remove'),
]
