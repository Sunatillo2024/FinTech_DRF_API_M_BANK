from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal
from authentication.models import User
from wallets.models import Wallet


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAW', 'Withdraw'),
        ('TRANSFER', 'Transfer'),
        ('PAYMENT', 'Payment'),
    )

    STATUS_CHOICES = (
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
    )

    # Asosiy maydonlar
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    currency = models.CharField(max_length=3, default='USD')

    # Foydalanuvchi va hamyon bog'lanishlari
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')

    # Transfer/Payment uchun qabul qiluvchi
    recipient = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='received_transactions'
    )
    recipient_wallet = models.ForeignKey(
        Wallet,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='received_transactions'
    )

    # Tranzaksiya tafsilotlari
    description = models.TextField(blank=True)
    fee = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    net_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    # Xavfsizlik va monitoring
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    is_fraudulent = models.BooleanField(default=False)
    fraud_check_performed = models.BooleanField(default=False)

    # Vaqt belgilari
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['status', 'created_at']),
            models.Index(fields=['transaction_type', 'created_at']),
        ]

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} {self.currency} - {self.status}"

    def save(self, *args, **kwargs):
        # Net amount ni hisoblash
        self.net_amount = self.amount - self.fee
        super().save(*args, **kwargs)

    def mark_as_completed(self):
        self.status = 'COMPLETED'
        self.completed_at = timezone.now()
        self.save()

    def mark_as_failed(self, reason=""):
        self.status = 'FAILED'
        self.description = f"{self.description}. Failed: {reason}" if self.description else f"Failed: {reason}"
        self.save()


from django.db import models

# Create your models here.
