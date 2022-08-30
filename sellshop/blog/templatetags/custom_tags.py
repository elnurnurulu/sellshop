
from django.template import Library
from blog.models import Blog
from product.models import ProductVersion

register = Library()


@register.simple_tag
def get_blogs(offset, limit, order):
    if order > 0:
        return Blog.objects.all().order_by('created_at')[offset:limit]
    return Blog.objects.all().order_by('-created_at')[offset:limit]

@register.simple_tag
def related_blog_categories(offset,limit):
    return Blog.objects.all().order_by('category')[offset:limit]

@register.simple_tag
def featured_product(offset,limit):
    return ProductVersion.objects.filter(featured=True).order_by('-featured')[offset:limit]