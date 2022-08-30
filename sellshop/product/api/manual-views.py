from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import ProductVersion
from product.api.serializers import ProductReadSerializer,ProductCreateSerializer
from rest_framework.status import ( 
    HTTP_200_OK, 
    HTTP_201_CREATED, 
    HTTP_204_NO_CONTENT
)
from django.http import Http404

class ProductApi(APIView):
    

    def get(self, request, *args, **kwargs):
        products = ProductVersion.objects.all() 
        category = request.GET.get('category') 
        tags = request.GET.get('tags') 
        if category:
            products = products.filter(category__id=category) 
        if tags:
            products = products.filter(tags__id=tags) 
        serializer = ProductReadSerializer(products, many=True, context={'request': request})
        return Response(data=serializer.data)


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)

class ProductDetailApi(APIView):

    def get(self, request, *args, **kwargs):
        product = ProductVersion.objects.filter(id=kwargs['pk']).first()
        if not product:
            raise Http404
        serializer = ProductReadSerializer(product, context={'request': request})
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        product = ProductVersion.objects.filter(id=kwargs['pk']).first()
        if not product:
            raise Http404
        serializer = ProductCreateSerializer(data=request.data, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        product = ProductVersion.objects.filter(id=kwargs['pk']).first()
        if not product:
            raise Http404
        serializer = ProductCreateSerializer(data=request.data, partial=True, instance=product)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        deleted_count, _ = ProductVersion.objects.filter(id=kwargs['pk']).delete()
        if deleted_count == 0:
            raise Http404
        return Response(data={}, status=HTTP_204_NO_CONTENT)