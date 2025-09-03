from django.db.models.signals import post_save
from django.dispatch import receiver
from authentication.models import User
from .models import Wallet

@receiver(post_save, sender=User)
def create_default_wallet(sender, instance, created, **kwargs):
    if created:
        # Yangi foydalanuvchi uchun default USD hamyon yaratish
        Wallet.objects.create(
            user=instance,
            currency='USD',
            balance=0.00,
            is_active=True
        )