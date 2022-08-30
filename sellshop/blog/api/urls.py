from django.urls import path
from blog.api import views as api_views

urlpatterns = [
   path('blogs/', api_views.BlogListCreateAPIView.as_view(), name='blog-list' ),
   path('blogs/<int:pk>', api_views.BlogDetailAPIView.as_view(), name='blog-detail'),
   path('blogs/<int:blog_pk>/comments', api_views.BlogCommentListCreateAPIView.as_view(), name='blog-comment'),

   path('blog-categories/', api_views.BlogCategoryListCreateAPIView.as_view(), name='blog-categories'),
   path('blog-categories/<int:pk>', api_views.BlogCategoryRetrieveUpdateDestroyAPIView.as_view(), name='blog-categories-detail'),

   path('blog-comments/<int:pk>', api_views.BlogCommentDetailAPIView.as_view(), name='blog-comment-detail'),
]