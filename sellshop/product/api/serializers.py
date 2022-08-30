from rest_framework import serializers
from product.models import (Category, Brand, Product, Tag, Color, Size, ProductVersion, ProductImage, ProductReview, Discount)

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
    

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    product_versions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-version-detail',
    )
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

class ProductVersionSerializer(serializers.ModelSerializer):
    product_reviews = ProductReviewSerializer(many=True, required=False)
    images = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)
    color = ColorSerializer()
    size = SizeSerializer()
    discount = DiscountSerializer()

    def get_images(self, product_version):
       return ProductImageSerializer(product_version.product_images.all(), many=True).data
       
    class Meta:
        fields = '__all__'
        model = ProductVersion
        read_only_fields = ['id', 'user', 'created_at', 'title', 'product_reviews', 'updated_at']


class ProductSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)
    product_versions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-version-detail',
    )
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class CategorySerializer(serializers.ModelSerializer):
    category_products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail',
    )
    parent_cat = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = [
        "id",
        "title",
        "category_products",
        "parent_cat",
        ]
        read_only_fields = ['id', 'title_en','title_az', 'created_at', 'updated_at']

    def get_parent_cat(self,obj):
        if obj.parent_cat:
            return obj.parent_cat.title
        return "None"















