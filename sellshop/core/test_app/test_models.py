from django.test import TestCase
from core.models import Contact, Subscriber

class ContactTest(TestCase):
    
    def setUp(self):
        self.data = {
            "name" : "TestName",
            "email" : "Test@email.com"
        }
        self.contact = Contact.objects.create(**self.data)

    def test_model_data(self):
        self.assertEqual(self.data["name"], self.contact.name)

    def test_str_method (self):
        self.assertEqual(str(self.contact), self.data["name"])

    def tearDown(self):
        del self.contact


class SubscriberTest(TestCase):

    @classmethod
    def setUp(cls):
        cls.data = {
            "email" : "Test@email.com"
        }
        cls.subscriber = Subscriber.objects.create(**cls.data)

    def test_model_data(self):
        self.assertEqual(self.data["email"], self.subscriber.email)

    def test_str_method (self):
        self.assertEqual(str(self.subscriber), self.data["email"])

    @classmethod
    def tearDown(cls): #the test runner will invoke that method after each test and tearDown deletes contact object.
        del cls.subscriber