import imp
from celery import shared_task
import time
from pytz import timezone
from core.publisher import Publish
from product.models import ProductVersion
from .models import  Subscriber
from blog.models import Blog
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.db.models import Count
from datetime import *
from django.contrib.auth import get_user_model

User = get_user_model()


@shared_task
def process_func():
    time.sleep(10)
    return 'Process done'

@shared_task
def send_mail_to_subscribers():
    email_list = Subscriber.objects.filter(is_active = True).values_list('email',flat=True)
    today=datetime.now(timezone.utc)
    lastweek = today - timedelta(weeks=1)
    products = ProductVersion.objects.annotate(
        num_rev=Count('product_reviews')).filter(created_at__gte=datetime.now(timezone.utc)-timedelta(days=7)).order_by('-num_rev')[:3]
    mail_text = render_to_string('email-subscriber.html',{
        'products': products,
    })
    Publish(data={"body":mail_text,"subject":"Products for this week","recipients":list(email_list) ,"subtype":"html"},event_type="send_mail")
    # msg = EmailMultiAlternatives(subject='Blogs for this week', body=mail_text, from_email=settings.EMAIL_HOST_USER, to=email_list, )
    # msg.attach_alternative(mail_text, "text/html")
    # msg.send()
@shared_task
def send_mail_to_users():
    email_list = []
    users = User.objects.filter(is_active=True).values_list('last_login','username', 'email')
    for user in users:
        now = datetime.now(timezone.utc)
        if (now-user[0] > timedelta(days=30)):
            email_list.append(user[2])
    products = ProductVersion.objects.annotate(num_tags=Count('reviews')).filter(created_at__gte=datetime.now(timezone.utc)-timedelta(days=30)).order_by('-num_tags')[:5]
    mail_text = render_to_string('email-subscriber.html',{
        'products': products,
    })
    Publish(data={"body":mail_text,"subject":"Products for this week","recipients":list(email_list) ,"subtype":"html"},event_type="send_mail")