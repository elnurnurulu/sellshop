from django.db import models
# Create your models here.
from django.contrib.auth import get_user_model
from traitlets import default
from product.models import ProductVersion
from sellshop.utils.abstract_models import AbstrasctModel
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

class Country(AbstrasctModel):
    country = CountryField(
        verbose_name="Country", max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return f"{self.country}"

    class Meta:
        verbose_name_plural = "Countries"

class ShippingAddress(AbstrasctModel):
    user        = models.ForeignKey(User, on_delete=models.CASCADE,related_name="shipping_address")

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    address   = models.CharField(max_length=100)
    default = models.BooleanField(default=False)
    city        = models.CharField(max_length=50)
    zipcode     = models.CharField(max_length=50)
    country     = models.ForeignKey(Country,on_delete=models.CASCADE, max_length=50)
    phone       = PhoneNumberField(blank=True, null=True)

    def __str__(self) -> str:
        return self.address

    class Meta:
        verbose_name = "Shipping Address"
        verbose_name_plural = "Shipping Addresses"


class BillingAddress(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, default='',related_name="billing_address")

    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    address     = models.CharField(max_length=100)
    city        = models.CharField(max_length=50)
    zipcode     = models.CharField(max_length=50)
    country     = models.CharField(max_length=50)
    phone       = PhoneNumberField(blank=True, null=True)

    def __str__(self) -> str:
        return self.address

    class Meta:
        verbose_name = "Billing Address"
        verbose_name_plural = "Billing Addresses"


class Wishlist(AbstrasctModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="",related_name="wishlistofUser")
    product = models.ManyToManyField(ProductVersion, blank=True, related_name='Product_wishlist')

    def __str__(self):
        return f"{self.user}"


class Order(AbstrasctModel):
    basket = models.OneToOneField('Basket', default='', on_delete=models.CASCADE)

    total = models.DecimalField('Total', decimal_places=2, max_digits=10)

    def __str__(self):
        return str(self.total)


class Basket(AbstrasctModel):
    author = models.ForeignKey(User, default='', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)  ##### status = is_ordered
    product = models.ManyToManyField(
        ProductVersion, blank=True)
    ordered_at = models.DateTimeField(
        verbose_name="Ordered at", null=True, blank=True)
    shipping_address = models.OneToOneField(
        ShippingAddress, null=True, blank=True, verbose_name="Shipping Address", on_delete=models.CASCADE)
    sub_total = models.DecimalField('Sub Total', decimal_places=2, max_digits=10,)

    def __str__(self):
        return str(self.status)


class BasketItem(AbstrasctModel):
    basket = models.ForeignKey(Basket, default='', related_name='basketitems', on_delete=models.CASCADE)
    productVersion = models.ForeignKey(ProductVersion, related_name='Product_Cart',default='', on_delete=models.CASCADE, verbose_name='Product Version')

    price = models.DecimalField('Price', decimal_places=2, max_digits=10)
    sub_total = models.DecimalField('Sub-Total', decimal_places=2, max_digits=10)
    count = models.IntegerField('Count')

    def __str__(self):
        return str(self.sub_total)
