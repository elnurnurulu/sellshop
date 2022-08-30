from django.urls import path
from product.api import views as api_views


urlpatterns = [
    path('categories/', api_views.CategoryListCreateAPIView.as_view(), name="category-list"),
    path('categories/<int:pk>', api_views.CategoryDetailAPIView.as_view(), name="category-detail"),

    path('products/', api_views.ProductListCreateAPIView.as_view(), name="product_list"),
    path('products/<int:pk>', api_views.ProductDetailAPIView.as_view(), name="product-detail"),

    path('product-versions/', api_views.ProductVersionListCreateAPIView.as_view(), name="product-version-list"),
    path('product-versions/<int:pk>', api_views.ProductVersionDetailAPIView.as_view(), name="product-version-detail"),
    path('product-versions/<int:product_version_pk>/images', api_views.ProductImageListCreateAPIView.as_view(), name='product-version-images'),
    path('product-versions/<int:product_version_pk>/reviews', api_views.ProductReviewListCreateAPIView.as_view(), name='product-version-images'),

    path('colors/', api_views.ColorListCreateAPIView.as_view(), name="color-list"),
    path('sizes/', api_views.SizeListCreateAPIView.as_view(), name="size-list"),
    path('tags/', api_views.TagListCreateAPIView.as_view(), name="tag-list"),

    path('product-images/<int:pk>', api_views.ProductImageDetailAPIView.as_view(), name="product-image-detail"),

    path('product-reviews/', api_views.ProductReviewListCreateAPIView.as_view(), name="product-review-list"),
    path('product-reviews/<int:pk>', api_views.ProductReviewDetailAPIView.as_view(), name="product-review-detail"),

    path('brands/', api_views.BrandListCreateAPIView.as_view(), name="brand-list"),
    path('brands/<int:pk>', api_views.BrandDetailAPIView.as_view(), name="brand-detail"),
]


