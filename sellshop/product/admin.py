from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from csv import *
from nested_admin import NestedModelAdmin, NestedTabularInline, NestedStackedInline

from product.models import (Category, Brand, Discount, Product, Tag, Color, Size, ProductVersion, ProductImage, ProductReview)
myModels = [Category, Brand, Tag, Color, Size, ProductReview, Discount,]
admin.site.register(myModels)


class ProductImageInline(NestedTabularInline):
    model = ProductImage
    extra = 5

class ProductVersionInline(NestedStackedInline):
    model = ProductVersion
    extra = 1
    inlines = [ProductImageInline,]
    classes = ["collapse"]

    list_filter = ('color', 'size' )
    exclude = ('title',)


class ProductAdmin(NestedModelAdmin):
    inlines = [ProductVersionInline,]


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'parent_cat',)
    list_filter = ('title',)
    search_fields = ('title', )
    classes = ['collapse']
    

class ProductImagesAdmin(TranslationAdmin):
    list_display = ('image', 'product_version','is_main' )
    list_filter = ('product_version',)
    search_fields = ('product_version','image' )
    fieldsets = [
        ('Standard info', {
            'fields': ('product_version','image', 'is_main' ),
            'classes': ('collapse',)
        }),
    ]


class ProductReviewsAdmin(TranslationAdmin):
    list_filter = ('user', 'rating',)
    search_fields = ('review', 'user', 'rating',)
    readonly_fields = ["user",]
    ordering = ('-confirm',)


class BrandAdmin(TranslationAdmin):
    list_display = ('title',)


class DiscountAdmin(TranslationAdmin):
    list_display = ('title',)


class TagAdmin(TranslationAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)


class ColorAdmin(TranslationAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)


class SizeAdmin(TranslationAdmin):
    list_display = ('title', )
    list_filter = ('title',)
    search_fields = ('title',)
