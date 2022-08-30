from django.urls import path
from pyparsing import delimited_list
from order.api import views

urlpatterns = [
    path('carts/', views.BasketViewAPI.as_view(), ),
    path('cartitems/', views.BasketItemViewAPI.as_view(), ),
    path('cartitems/<int:pk>/', views.BasketItemRetrieveUpdateDestroyAPIView.as_view(),),
    path('wishlist/', views.WishlistAPIView.as_view(), name='wishlist_api'),
   

]