from django.test import TestCase

from rest_framework.test import APIRequestFactory

# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})


# Create a JSON POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'}, format='json')




# from multiprocessing.sharedctypes import Value
# from unicodedata import category, name
# from django.test import TestCase
# from django.urls import reverse_lazy
# from product.models import Category, User, Product, PropertyValues, PropertyName, Brand
# from django.conf import settings


# class TestProductsAPIView(TestCase):

#     @classmethod
#     def setUpClass(cls):
#         cls.url = reverse_lazy('api_products')
#         cls.category = Category.objects.create(name='Cat 1')
#         cls.user = User.objects.create_user(username='numan', email='numan@gmail.com', password='numan123')
#         cls.brand = Brand.objects.create(name='brand')
#         cls.propertyname = PropertyName.objects.create(category=cls.category, name='lkl')
#         cls.property = PropertyValues.objects.create(propertyname=cls.propertyname, value='def')
#         cls.product = Product.objects.create(brand=cls.brand, category= cls.category, title='abc')
        

#     def test_api_url(self):
#         expected_url = '/api/products/'
#         self.assertEqual(self.url, expected_url)


#     def test_api_post_request_status_code(self):
#         valid_data = {
#             'product': self.product.id,
#             'property': self.property.id,
#             'title': 'STORY #1',
#             # 'category': self.cat.id,
#             # 'author': self.user.id,
#             # 'image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
#             # 'cover_image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
#             'code': '123',
#             'price': '12',
#             'stock': 1
#         }
#         res = self.client.post(self.url, data=valid_data)
#         self.assertEqual(res.status_code, 201)


#     def test_api_post_request_valid_data_response(self):
#         valid_data = {
#             'product': self.product.id,
#             'property': self.property.id,
#             'title': 'STORY #1',
#             # 'category': self.cat.id,
#             # 'author': self.user.id,
#             # 'image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
#             # 'cover_image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
#             'code': '123',
#             'price': '12',
#             'stock': 1
#         }
#         res = self.client.post(self.url, data=valid_data)
#         result = res.json()
#         self.assertEqual(result['title'], valid_data['title'])


#     def test_api_post_request_invalid_data_response(self):
#         in_valid_data = {
#             'product': 'llll',
#             'property': self.property.id,
#             'title': 'STORY #1',
#             # 'category': self.cat.id,
#             # 'author': self.user.id,
#             # 'image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
#             # 'cover_image': ('1_1Y7ahYk.png', open(f'{settings.MEDIA_ROOT}/story_images/1_1Y7ahYk.png', 'rb')),
#             'code': '123',
#             'price': '12',
#             'stock': 1
#         }
#         res = self.client.post(self.url, data=in_valid_data)
#         result = res.json()
#         self.assertIn('Incorrect type. Expected pk value, received str.', result['product'])


#     def test_api_get_request_response(self):
#         res = self.client.get(self.url)
#         self.assertIsInstance(res.json(), list)


#     def test_api_get_request_status_code(self):
#         res = self.client.get(self.url)
#         self.assertEqual(res.status_code, 200)


#     @classmethod
#     def tearDownClass(cls):
#         ...