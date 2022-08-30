from django.urls import path
from . import views as template_views

urlpatterns = [
   path('blogs',template_views.BlogListView.as_view(), name="blogs"),  
   path('blogs/<slug:slug>/',template_views.BlogDetailView.as_view(), name="blog_detail"),  
]
