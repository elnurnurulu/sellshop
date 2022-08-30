from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):

    SEX_CHOICES = (
        ('mr', 'mr'),
        ('mrs', 'mrs'),
    )
    
    email = models.EmailField(('email address'), blank=True, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='profile_images')
    sex = models.CharField(max_length=40, choices=SEX_CHOICES)
    phone_number = models.TextField(max_length=500, blank=True)
    birthdate = models.DateField(max_length=500, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return str(self.username)

    @property
    def basket(self):
        return self.basket_set.filter(status=False).last()

# class BillingAddress(AbsrtactModel):

#     COUNTRY_CHOICES = (
#         ('Bangladesh', 'Bangladesh'),
#         ('United States', 'United States'),
#         ('UNited KIngdom', 'UNited KIngdom'),
#         ('Canada', 'Canada'),
#         ('Malaysia', 'Malaysia'),
#         ('United Arab Emirates', 'United Arab Emirates')
#     )

#     TOWN_CHOICES = (
#         ('Aberdeen','Aberdeen'),
#         ('Bedfordshire','Bedfordshire'),
#         ('Caerphilly','Caerphilly'),
#         ('Denbighshire','Denbighshire'),
#         ('East Ayshire','East Ayshire'),
#         ('Falkirk','Falkirk')
#     )

#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField(max_length=40)
#     country = models.CharField(max_length=40, choices=COUNTRY_CHOICES)
#     address = models.CharField(max_length=255)
#     town = models.CharField(max_length=40, choices=TOWN_CHOICES)
#     mobile_phone = models.IntegerField()
#     information = models.TextField()
#     reference = models.CharField(max_length=40,blank=True)