from django.contrib import admin

from django.contrib import admin
from .models import Wallet

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'currency', 'balance', 'is_active']
    list_filter = ['currency', 'is_active']
    search_fields = ['user__username']