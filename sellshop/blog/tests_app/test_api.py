from django.test import TestCase
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from blog.models import BlogBrand, BlogCategory, Blog, BlogComment
from django.conf import settings

User = get_user_model()

class TestStoriesAPIView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = reverse_lazy('blog-list')
        cls.cat = BlogCategory.objects.create(title='Cat 1',)
        cls.brand = BlogBrand.objects.create(title='Brand 1',)
        cls.user = User.objects.create_user(username='Test', email='test@gmail.com', password='testpassword0123456')

    def test_api_url(self):
        expected_url = '/api/blogs/'
        self.assertEqual(self.url, expected_url)

    # def test_api_post_request_status_code(self):
    #     valid_data = {
    #         'author' : self.user.id,
    #         'category' : self.cat.id,
    #         'brand' : self.brand.id,
    #         'title' : "Test Blog" ,
    #         # 'image' : ('test.png', open(f'{settings.MEDIA_ROOT}/blog_images/test.png', 'rb')),
    #         'description' : "Test Description" ,
    #         'content' : "Test Content" ,
    #         'slug' : "Test-Blog",
    #     }
    #     res = self.client.post(self.url, data=valid_data)
    #     self.assertEqual(res.status_code, 201)

    # def test_api_post_request_valid_data_response(self):
    #     valid_data = {
    #         'author' : self.user.id,
    #         'category' : self.cat.id,
    #         'brand' : self.brand.id,
    #         'title' : "Test Blog" ,
    #         # 'image' : ('test.png', open(f'{settings.MEDIA_ROOT}/blog_images/test.png', 'rb')),
    #         'description' : "Test Description" ,
    #         'content' : "Test Content" ,
    #         'slug' : "Test-Blog",
    #     }
    #     res = self.client.post(self.url, data=valid_data)
    #     result = res.json()
    #     self.assertEqual(result['title'], valid_data['title'])

    def test_api_post_request_invalid_data_response(self):
        in_valid_data = {
            'author' : self.user.id,
            'category' : self.cat.id,
            'brand' : self.brand.id,
            # 'image' : ('test.png', open(f'{settings.MEDIA_ROOT}/blog_images/test.png', 'rb')),
            'description' : "Test Description" ,
            'content' : "Test Content" ,
            'slug' : "Test-Blog",
        }
        res = self.client.post(self.url, data=in_valid_data)
        result = res.json()
        self.assertIn('This field is required.', result['title'])

    def test_api_get_request_response(self):
        res = self.client.get(self.url)
        self.assertIsInstance(res.json(), list)

    # def test_api_get_request_status_code(self):
    #     res = self.client.get(self.url)
    #     self.assertEqual(res.status_code, 200)

    @classmethod
    def tearDownClass(cls):
        del cls.url
        del cls.cat
        del cls.user
        del cls.brand
