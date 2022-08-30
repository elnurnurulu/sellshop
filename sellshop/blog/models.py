from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField

User = get_user_model()


class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BlogCategory(models.Model):
    parent_cat = models.ForeignKey('self', related_name='category_sub_cat', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Blog Category'
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.title


class BlogBrand(models.Model):
    title = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name = 'Blog brand'
        verbose_name_plural = 'Blog brands'

    def __str__(self):
        return self.title


class Blog(AbstractModel):
    author = models.ForeignKey(User, related_name='author_blogs', on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(BlogCategory, related_name='category_blogs', on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250, db_index=True)
    image = models.ImageField(upload_to='blog_images')
    description = models.CharField(max_length=255)
    content = RichTextField()
    slug = models.SlugField(max_length=70, editable=False, db_index=True) 


    def get_absolute_url(self):
        return reverse_lazy('blog_detail', kwargs={
            'slug': self.slug
        })


    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title


class BlogComment(AbstractModel):
    parent_comment = models.ForeignKey('self', related_name='child_comments', on_delete=models.CASCADE, null=True, blank=True, )
    blog = models.ForeignKey(Blog, related_name='blog_comments', on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, related_name='user_blog_comments', on_delete=models.CASCADE, default=1)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Blog comment'
        verbose_name_plural = 'Blog comments'

    def __str__(self):
        return f'{self.comment} - {self.blog} ({self.user})' 

    def children(self):
        return BlogComment.objects.filter(parent_comment=self)

    @property
    def is_parent(self):
        if self.parent_comment is not None:
            return False
        return True



