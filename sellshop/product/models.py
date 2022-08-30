from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from sellshop.utils.abstract_models import AbstrasctModel


User = get_user_model()


class Category(models.Model):
    parent_cat = models.ForeignKey('self', related_name='sub_categories', on_delete=models.CASCADE, null=True, blank=True,)
    title = models.CharField(max_length=50, db_index=True)
    
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    
    def __str__(self):
        if self.parent_cat:
            return f'{self.title} - {self.parent_cat}'
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(verbose_name="Title", max_length=30, help_text="Max 30 char.") 

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(verbose_name="Title",
                             max_length=30, help_text="Max 30 char.")
    class Meta:
        verbose_name = 'Size'
        verbose_name_plural = 'Sizes'

    def __str__(self):
        return self.title


class Product(AbstrasctModel):
    category = models.ForeignKey(Category, related_name='category_products', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.CASCADE, default="1")
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=True, blank=True)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title

    def is_featured(self):
        return self.featured


class Discount(AbstrasctModel):
    title=models.CharField('Title', max_length=80)
    percentage=models.CharField('Percentage', max_length=20, null=True, blank=True)
    value=models.IntegerField('Value', null=True, blank=True)

    def __str__(self):
        return self.title


class ProductVersion(AbstrasctModel):
    title = models.CharField(max_length=100, db_index=True,)
    product = models.ForeignKey(Product, related_name='product_versions', on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(Color, related_name='same_color_product_versions', on_delete=models.CASCADE, default="1")
    size = models.ForeignKey(Size, related_name='same_size_product_versions', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    old_price = models.DecimalField(verbose_name = "Price", decimal_places = 2, max_digits=6,)
    discount = models.ForeignKey('Discount', related_name='product_discount', on_delete=models.CASCADE, blank=True, null=True,)
    new_price = models.DecimalField(verbose_name = "Discounted Price", decimal_places = 2, max_digits=6, null=True, blank=True, help_text="""
        Buraya hər hansı məbləğ qeyd etməyə ehtiyac yoxdur. Daxil etdiyiniz qiymət və endirim (əgər varsa) nəzərə alınaraq avtomatik hesablanma aparılır.""")
    hide = models.BooleanField('Hide', default=False, help_text="Məhsulun səhifədə görünməsini dayandırmaq") 

    def get_absolute_url(self):
        return reverse_lazy ('single_product', kwargs = {
            'pk': self.id
        })

    class Meta:
        verbose_name = 'Product version'
        verbose_name_plural = 'Product versions'

    def __str__(self):
        return self.title


class ProductImage(AbstrasctModel):
    product_version = models.ForeignKey(ProductVersion, related_name='product_images', on_delete=models.CASCADE, default="1")
    image = models.FileField(upload_to='product_images',  null = True , blank = True)
    is_main = models.BooleanField('Main picture', default=False, help_text="Daxil etdiyiniz şəkillərdən yalnız birini məhsulun əsas şəkli olaraq seçin") 
    
    def __str__(self):
        return self.image.url

    class Meta:
        verbose_name = 'Product image'
        verbose_name_plural = 'Product images'


class ProductReview(AbstrasctModel):
    CHOICES = (
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )

    product_version = models.ForeignKey(ProductVersion, related_name='product_reviews', on_delete=models.CASCADE, null=True, default="1")
    user = models.ForeignKey(User, related_name='user_product_reviews', on_delete=models.CASCADE, editable=False, null=True, default="1")
    review = models.TextField()
    rating = models.IntegerField(choices=CHOICES, default=5, null=True, blank=True,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    confirm = models.BooleanField('Confirm', default=False, help_text="Confirm review") 

    class Meta:
        verbose_name = 'Product review'
        verbose_name_plural = 'Product reviews'

    def get_absolute_url(self):
        return reverse_lazy ('single_product', kwargs = {
            'pk': self.product_version.id
        })

    def __str__(self):
        if self.confirm:
            return f"{self.review} - Review is confirmed"
        return self.review



