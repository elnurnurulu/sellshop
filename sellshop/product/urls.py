
from django.urls import path
from product import views as template_views

urlpatterns = [
    path('products/',  template_views.ProductListView.as_view(), name='product'),
    path('products/<int:pk>/', template_views.ProductView.as_view(), name='single_product'),
    path('search/', template_views.SearchView.as_view(), name="search"),
    path('reviews/<int:pk>/', template_views.UpdateReviewView.as_view(), name='edit_review'),
]
