from django.test import TestCase
from django.urls import reverse_lazy


class TestContactView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.contact_page_url = reverse_lazy('contact')
        cls.valid_data = {
            'name': 'Test',
            'email': 'Test@gmail.com',
            'message': 'It is test message'
        }
        cls.invalid_data = {
            'name': """
            Lorem Ipsum is simply dummy text of the printing and typesetting 
            industry. Lorem Ipsum has been the industry's standard dummy text 
            ever since the 1500s, when an unknown printer took a galley of type 
            and scrambled it to make a type specimen book. It has survived not only 
            five centuries, but also the leap into electronic typesetting, remaining 
            essentially unchanged. It was popularised in the 1960s with the release of 
            """,
            'email': 'invalid email',
            'message': ''
        }

    def test_url(self):
        expected_contact_url = '/en/contact/'
        self.assertEqual(self.contact_page_url, expected_contact_url)

    def test_contact_page_status_code(self):
        res = self.client.get(self.contact_page_url)
        self.assertEqual(res.status_code, 200)

    def test_contact_page_template_name(self):
        res = self.client.get(self.contact_page_url)
        self.assertTemplateUsed(res, 'contact.html')

    def test_contact_page_context(self):
        res = self.client.get(self.contact_page_url)
        self.assertTrue(res.context['form'])

    def test_contact_page_post_request_status_code(self):
        res = self.client.post(self.contact_page_url, self.valid_data)
        self.assertRedirects(res, reverse_lazy('index'), )

    def test_contact_page_post_request_invalid_data(self):
        res = self.client.post(self.contact_page_url, self.invalid_data)
        form = res.context['form']
        self.assertTrue(form.errors)

    @classmethod
    def tearDownClass(cls):
        del cls.contact_page_url
        del cls.valid_data
        del cls.invalid_data


class TestSubscribeView(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.subscribe_page_url = reverse_lazy('subscribe')
        cls.valid_data = {
            'email': 'Test@gmail.com',
        }
        cls.invalid_data = {
            'email': 'invalid email',
        }

    def test_url(self):
        expected_subscribe_url = '/en/subscribe/'
        self.assertEqual(self.subscribe_page_url, expected_subscribe_url)

    def test_subscribe_page_status_code(self):
        res = self.client.get(self.subscribe_page_url)
        self.assertEqual(res.status_code, 200)

    def test_subscribe_page_template_name(self):
        res = self.client.get(self.subscribe_page_url)
        self.assertTemplateUsed(res, 'index.html')

    def test_subscribe_page_context(self):
        res = self.client.get(self.subscribe_page_url)
        self.assertTrue(res.context['form'])

    def test_subscribe_page_post_request_status_code(self):
        res = self.client.post(self.subscribe_page_url, self.valid_data)
        self.assertRedirects(res, reverse_lazy('index'), )

    def test_subscribe_page_post_request_invalid_data(self):
        res = self.client.post(self.subscribe_page_url, self.invalid_data)
        form = res.context['form']
        self.assertTrue(form.errors)

    @classmethod
    def tearDownClass(cls):
        del cls.subscribe_page_url
        del cls.valid_data
        del cls.invalid_data

