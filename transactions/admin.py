from django.contrib import admin
from .models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user', 'transaction_type', 'status', 'amount', 'currency',
        'recipient', 'created_at', 'is_fraudulent'
    ]
    list_filter = ['transaction_type', 'status', 'currency', 'is_fraudulent', 'created_at']
    search_fields = ['user__username', 'recipient__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at', 'completed_at']
    list_per_page = 20

    fieldsets = (
        ('Basic Information', {
            'fields': ('user', 'transaction_type', 'status', 'amount', 'currency')
        }),
        ('Wallet Information', {
            'fields': ('wallet', 'recipient', 'recipient_wallet')
        }),
        ('Details', {
            'fields': ('description', 'fee', 'net_amount')
        }),
        ('Security', {
            'fields': ('is_fraudulent', 'fraud_check_performed', 'ip_address', 'user_agent')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'completed_at')
        }),
    )