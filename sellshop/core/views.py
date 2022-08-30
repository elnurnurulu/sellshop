from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm ,SubscribeForm
from django.contrib import messages
from django.views.generic import CreateView
from product.models import ProductVersion
from blog.models import Blog
from django.db.models import Count


def about(request):
    return render(request,'about.html')

def error404(request):
    return render(request,'error-404.html')

def index(request):
    queryset = ProductVersion.objects.filter(hide=False, quantity__gt=0)

    mostreview = queryset.annotate(num_rev=Count('product_reviews')).order_by('-num_rev')[:4]
    new_arrivals = queryset.order_by("-created_at")[:3]
    featured_products = queryset.filter(product__featured=True)[:6]
    bestseller = queryset.annotate(mostsold=Count('Product_Cart')).order_by('-mostsold')[1:8]
    firstbestseller = queryset.annotate(mostsold=Count('Product_Cart')).order_by('-mostsold')[0] if queryset.count() > 0 else None
    latest_blog = Blog.objects.order_by("-created_at")[:3]

    context = {
        'title': 'Home Sellshop',
        'featured_products': featured_products,
        'new_arrivals': new_arrivals,
        'latest_blog': latest_blog,
        'bestseller': bestseller,
        'firstbestseller': firstbestseller,
        'productversions': queryset,
        'mostreview': mostreview,
    }

    return render(request,'index.html',context=context)


class ContactView(CreateView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Mesajiniz qeyde alindi!')
        return result


class SubscribeView(CreateView):
    template_name = 'index.html'
    form_class = SubscribeForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        result = super().form_valid(form)
        messages.add_message(self.request, messages.SUCCESS, 'Email qeyde alindi!')
        return result