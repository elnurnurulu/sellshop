from urllib import request
from rest_framework.response import Response
from order.api.serializers import (
    BasketSerializer,
    BasketReadItemSerializer,
    BasketCreateItemSerializer,
    WishlistSerializer
)
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status,permissions
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.http import Http404
from order.models import *
from product.models import *


User = get_user_model()


class CustomListCreateAPIView(ListCreateAPIView):

    def get_serializer_class(self):
        return self.serializer_classes.get(self.request.method)


class BasketViewAPI(ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class BasketItemViewAPI(CustomListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = BasketItem.objects.all()
    serializer_classes = {
        'POST': BasketCreateItemSerializer,
        'GET': BasketReadItemSerializer
    }


    def get_queryset(self):
        user = self.request.user
        return super().get_queryset().filter(basket__author=user).exclude(basket__status = True).order_by('-created_at')


class BasketItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = BasketItem.objects.all()
    

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BasketReadItemSerializer
        else:
            return BasketCreateItemSerializer

class WishlistAPIView(APIView):
    serializer_class = WishlistSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(responses={200: WishlistSerializer(many=True)})
    def get(self, request, *args, **kwargs):
        obj, created = Wishlist.objects.get_or_create(user=request.user)
        serializer = self.serializer_class(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(operation_description="description")
    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        product = ProductVersion.objects.get(pk=product_id)
        Wishlist.objects.get_or_create(user=request.user)
        wishlist = Wishlist.objects.get(user=request.user)
        if product and product not in wishlist.product.all():
            wishlist.product.add(product)
        else:
            wishlist.product.remove(product)
        message = {'success': True,
                   'message': 'Product added to your wishlist.'}
        return Response(message, status=status.HTTP_201_CREATED)