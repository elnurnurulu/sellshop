
from django.contrib.auth import get_user_model

from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from order.models import BasketItem, Basket,Wishlist
from user.api.serializers import *
from product.api.serializers import *


User = get_user_model()


class BasketSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    basketitem = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = (
            'author',
            'basketitem',
            'sub_total',
            'status',
        )


    def get_basketitem(self, obj):
        items = obj.basketitems.all().values_list('id', "productVersion", 'price', 'sub_total', 'count')
        item_list = []
        for item in items:
            item_list.append(
                {
                    'id': item[0],
                    'productVersion':item[1],
                    'price':item[2],
                    'sub_total':item[3],
                    'count':item[4],
                }
            )
        return item_list


class BasketReadItemSerializer(serializers.ModelSerializer):
    productVersion = ProductVersionSerializer()
    basket = BasketSerializer()

    class Meta:
        model = BasketItem
        fields = (
            'id',
            'basket',
            'productVersion',
            'price',
            'sub_total',
            'count',
        )


class BasketCreateItemSerializer(serializers.ModelSerializer):
    productVersion = str(ProductVersionSerializer())
    # basket = str(BasketSerializer())
    
    class Meta:
        model = BasketItem
        fields = (
            'id',
            'productVersion',
            'price',
            'sub_total',
            'count',
        )

    def validate(self, data):
        context = self.context
        user = context['request'].user
        basket = user.basket
        print(basket)
        if not basket:
            basket = Basket.objects.create(author=user, sub_total=0)
        data['basket'] = basket
        return super().validate(data)



class WishlistSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Wishlist
        fields = '__all__'

    def get_product(self, obj):
        qs = obj.product.all()
        return ProductVersionSerializer(qs, many=True).data