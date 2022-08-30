
from django.urls import path
from order.views import cart, wish,order,CheckoutShipping,checkout

urlpatterns = [
    path('cart/', cart, name='cart'),
    path('wishlist/', wish, name='wishlist'),
    path('checkout/', checkout, name='checkout'),
    path('order/', order, name='order'),

]
