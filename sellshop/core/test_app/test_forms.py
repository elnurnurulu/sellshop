from django.test import TestCase
from core.forms import ContactForm, SubscribeForm


class TestContactForm(TestCase):

    @classmethod
    def setUpClass(cls):
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
        cls.valid_form = ContactForm(data=cls.valid_data)
        cls.invalid_form = ContactForm(data=cls.invalid_data)


    def test_form_with_valid_data(self):
        self.assertTrue(self.valid_form.is_valid())

    def test_form_with_invalid_data(self):
        self.assertFalse(self.invalid_form.is_valid())

    def test_error_email_field(self):
        self.assertIn('email', self.invalid_form.errors)

    def test_error_message_field(self):
        self.assertIn('message', self.invalid_form.errors)

    def test_error_messages(self):
        self.assertIn('Ensure this value has at most 255 characters (it has 483).', self.invalid_form.errors['name'])

    @classmethod
    def tearDownClass(cls):
      del cls.valid_form
      del cls.invalid_form


class TestSubscribeForm(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valid_data = {
            'email': 'Test@gmail.com',
        }
        cls.invalid_data = {
            'email': 'invalid email',
        }
        cls.valid_form = SubscribeForm(data=cls.valid_data)
        cls.invalid_form = SubscribeForm(data=cls.invalid_data)


    def test_form_with_valid_data(self):
        self.assertTrue(self.valid_form.is_valid())

    def test_form_with_invalid_data(self):
        self.assertFalse(self.invalid_form.is_valid())

    def test_error_email_field(self):
        self.assertIn('email', self.invalid_form.errors)

    def test_error_messages(self):
        self.assertIn('Enter a valid email address.', self.invalid_form.errors['email'])

    @classmethod
    def tearDownClass(cls):
      del cls.valid_form
      del cls.invalid_form