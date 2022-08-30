from django.contrib import admin

# Register your models here.
from order.models import *


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'zipcode']
    list_filter = ['user', 'city']
    search_fields = ['customer']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('basket', 'total', 'created_at')
    list_filter = ('basket', 'created_at')
    search_fields = ('basket', )


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('author', 'sub_total', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('author__username', )


@admin.register(BasketItem)
class BasketItemAdmin(admin.ModelAdmin):
    list_display = ('basket', 'productVersion', 'price', 'sub_total', 'count', 'created_at')
    list_filter = ('basket', 'created_at')
    search_fields = ('productVersion', )


# @admin.register(BasketItem)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('basket', 'price', 'count','product_version', )
#     list_filter = ('basket','product_version',)
#     search_fields = ('product_version', )
#     fieldsets = [
#         ('Standard info', {
#             'fields': ('basket',  ),
#             'classes': ('collapse',)
#         }),
#         # ('Other', {
#         #     'fields': ('tags', )
#         # }),
#     ]

# admin.site.register([Basket ])

admin.site.register([Wishlist,BillingAddress,Country])
