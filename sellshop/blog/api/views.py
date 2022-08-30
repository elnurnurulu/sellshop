from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


from blog.api.serializers import BlogSerializer, BlogCommentSerializer, BlogCategorySerializer
from blog.models import BlogCategory, Blog, BlogComment


class BlogCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogCategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    # get filtered data
    # http://127.0.0.1:8000/api/blogs/?category=2
    def get(self, request, *args, **kwargs):
        queryset = Blog.objects.all()
        category = request.GET.get('category')
        if category:
            queryset = queryset.filter(category=category)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer

    # path('blogs/<int:blog_pk>/comments', api_views.BlogCommentListCreateAPIView.as_view(), name='blog-comment'),
    def perform_create(self, serializer):
        blog_pk = self.kwargs.get('blog_pk')
        blog = get_object_or_404(Blog, pk=blog_pk)
        serializer.save(blog=blog)

    def get_queryset(self):
        blog = self.kwargs.get('blog_pk')
        return super().get_queryset().filter(blog=blog)


class BlogCommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer  




