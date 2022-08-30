from django.shortcuts import render
# from order.models import Basket,BasketItem
from django.http.response import HttpResponseRedirect
from order.models import BasketItem, User,ShippingAddress,Basket,Order,Country
from product.models import ProductVersion
from django.http import JsonResponse
from order.forms import ShippingAddressForm
from django.views.generic.base import View
from datetime import datetime
# Create your views here.
def wish(request):
    if request.user.is_authenticated:
        return render(request, "wishlist.html")
    return render(request, "error-404.html")

    
def cart(request):
    if request.user.is_authenticated:
        return render(request, "cart.html")
    return render(request, "error-404.html")

	

def order(request):
    if request.user.is_authenticated:
        return render(request, "order-complete.html")
    return render(request, "error-404.html")

def checkout(request):
    try:
        cart = BasketItem.objects.filter(
            cart=Basket.objects.get(author=request.user, status=False))
        counter = 0
        for i in range(len(cart)):
            if cart[i].product.quantity > 0:
                counter += 1
    except:
        counter = 0
    if request.method == "POST":
        form = ShippingAddressForm(request.POST)
        shipping = ShippingAddress(
                user=request.user,
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                address=request.POST.get('address'),
                city=request.POST.get('city'),
                zipcode=request.POST.get('zipcode'),
                country=Country.objects.get(id=request.POST.get('country')),
                phone=request.POST.get('phone'),
            )
        shipping.save()
        basket=Basket.objects.filter(status=False).filter(author=request.user).update(
                status=True, shipping_address=shipping, ordered_at=datetime.now())
        print('basket:',basket)
        user_cart = Basket.objects.filter(author=request.user).filter(
                status=True).filter(shipping_address=shipping).first()
        print('user_cart:',user_cart)
        for i in range(len(BasketItem.objects.filter(basket=user_cart))):
                # mini = BasketItem.objects.filter(basket=user_cart)[i].quantity
                # print('mini:',mini)

                quantity = BasketItem.objects.filter(basket=user_cart)[i].productVersion.quantity - BasketItem.objects.filter(basket=user_cart)[i].count
                ProductVersion.objects.filter(id=BasketItem.objects.filter(
                    basket=user_cart)[i].productVersion.id).update(quantity=quantity)
        # BasketItem.objects.get_or_create(user=request.user, status=False)
    else:
        form = ShippingAddressForm()
    context = {
        'title': 'Checkout Sellshop',
        'shipping': form,
        'cart_products': counter,
    }
    if request.user.is_authenticated:
        return render(request, "checkout.html", context=context)
    return render(request, "error-404.html", context=context)

class CheckoutShipping(View):
    template_name = 'checkout.html'
    http_method_names = ['get', 'post']


    def get(self, request):
        form = ShippingAddressForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            
            form.save()
         
            return HttpResponseRedirect('/checkout')
        else:
            return render(request, 'checkout.html', {'form': form})



