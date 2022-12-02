from celery import shared_task
from django.conf import settings
from datetime import datetime, timedelta
from django.core.mail import send_mail, EmailMessage
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from .models import SubscriberUserModel, UserModel
from Product.models import ProductModel


@shared_task
def send_email_task(mail_subject, message, to_email):
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        return 'send'
    else:
        return 'error'


@shared_task
def send_famous_product_to_subscribe_user():
    last_one_week = datetime.now() - timedelta(days=7)
    subscriber_emails = [subscriber.email for subscriber in SubscriberUserModel.objects.all()]

    reviews = [(product.reviews.all().count(), product.id) for product in ProductModel.objects.filter(created_at__gte=last_one_week)]
    if len(reviews) == 0:
        return 'empty'
    else:
        reviews = reviews = [tuplee[1] for tuplee in sorted(reviews, reverse=True)[:3]]
        products = ProductModel.objects.filter(id__in = reviews)
        subject = 'Most seller product in this week'
        html_message = render_to_string('email-subscribers.html', {'products': products, 'emails': subscriber_emails})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, plain_message, from_email, subscriber_emails, html_message=html_message)
        return 'send'


@shared_task
def send_email_for_one_month_lost_user():
    last_one_month = datetime.now() - timedelta(days=30)
    users = [user.email for user in UserModel.objects.filter(last_login__lte = last_one_month)]
    reviews = [(product.reviews.all().count(), product.id) for product in ProductModel.objects.filter(created_at__gte=last_one_month)]
    if len(reviews) == 0 or len(users) == 0:
        return 'empty'
    else:
        reviews = [tuplee[1] for tuplee in sorted(reviews, reverse=True)[:5]]
        products = ProductModel.objects.filter(id__in = reviews)
        subject = 'Most seller product in this month'
        html_message = render_to_string('email-subscribers.html', {'products': products, 'emails': users, 'domain': 'http://127.0.0.1:8000/media/'})
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message=None, from_email=from_email, recipient_list= users, html_message=html_message)
        return 'send'
