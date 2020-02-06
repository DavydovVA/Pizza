from django.urls import path

from cart import views

urlpatterns = [
    path('add/<int:product_id>/', views.AddToCart.as_view(), name='add_to_cart'),
    path('cart/', views.ViewCart.as_view(), name='view_cart'),
    path('update/<int:product_id>', views.ChangeQuan.as_view(), name='update_quan'),
    path('updateuser/', views.ChangeUserInfo.as_view(), name='change_user_info'),
]
