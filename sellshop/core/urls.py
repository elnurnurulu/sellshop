
from django.urls import path
from core.views import about, error404, index, ContactView ,SubscribeView

urlpatterns = [
    path('about/', about, name='about'),
    path('error404/', error404, name='error404'),
    path('', index, name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]
