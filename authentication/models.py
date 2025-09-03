from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('auditor', 'Auditor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    phone_number = models.CharField(max_length=15, blank=True)
    requires_2fa = models.BooleanField(default=False)
    otp_secret = models.CharField(max_length=32, blank=True) # 2FA uchun

    def __str__(self):
        return self.username