# tasks.py yaratamiz
from celery import shared_task
from django.core.mail import send_mail
from .models import Transaction

@shared_task
def check_transaction_for_fraud(transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    # Fraud detection logikasi
    # ...
    if fraud_detected:
        transaction.mark_as_failed("Fraud detected")