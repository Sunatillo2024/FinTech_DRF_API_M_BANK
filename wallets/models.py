from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from authentication.models import User


class Wallet(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('UZS', 'Uzbekistan Som'),
        ('BTC', 'Bitcoin'),
        ('ETH', 'Ethereum'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wallets')
    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'currency', 'is_active']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s {self.currency} Wallet (Balance: {self.balance})"

    def deactivate(self):
        """Hamyonni faolsizlantirish"""
        self.is_active = False
        self.save()

    def activate(self):
        """Hamyonni faollashtirish"""
        # Bir xil valyutada boshqa faol hamyon yo'qligini tekshirish
        if Wallet.objects.filter(
                user=self.user,
                currency=self.currency,
                is_active=True
        ).exclude(id=self.id).exists():
            raise ValueError("You already have an active wallet with this currency.")

        self.is_active = True
        self.save()