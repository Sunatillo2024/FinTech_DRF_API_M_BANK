from rest_framework import serializers
from .models import Transaction
from wallets.models import Wallet
from django.db import transaction as db_transaction


class TransactionSerializer(serializers.ModelSerializer):
    wallet_currency = serializers.CharField(source='wallet.currency', read_only=True)
    recipient_email = serializers.EmailField(write_only=True, required=False)

    class Meta:
        model = Transaction
        fields = [
            'id', 'transaction_type', 'status', 'amount', 'currency',
            'wallet', 'wallet_currency', 'recipient', 'recipient_wallet',
            'recipient_email', 'description', 'fee', 'net_amount',
            'created_at', 'updated_at', 'completed_at'
        ]
        read_only_fields = [
            'id', 'status', 'net_amount', 'created_at', 'updated_at',
            'completed_at', 'recipient', 'recipient_wallet'
        ]

    def validate(self, data):
        # Tranzaksiya turi bo'yicha validatsiya
        transaction_type = data.get('transaction_type')
        amount = data.get('amount')
        wallet = data.get('wallet')

        if transaction_type in ['WITHDRAW', 'TRANSFER']:
            if wallet.balance < amount:
                raise serializers.ValidationError(
                    "Insufficient balance in the wallet."
                )

        if transaction_type == 'TRANSFER' and not data.get('recipient_email'):
            raise serializers.ValidationError(
                "Recipient email is required for transfer transactions."
            )

        return data


class TransactionDetailSerializer(serializers.ModelSerializer):
    wallet_info = serializers.SerializerMethodField()
    recipient_info = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            'id', 'transaction_type', 'status', 'amount', 'currency',
            'wallet', 'wallet_info', 'recipient', 'recipient_info',
            'description', 'fee', 'net_amount', 'is_fraudulent',
            'created_at', 'updated_at', 'completed_at'
        ]

    def get_wallet_info(self, obj):
        return {
            'id': obj.wallet.id,
            'currency': obj.wallet.currency,
            'balance': obj.wallet.balance
        }

    def get_recipient_info(self, obj):
        if obj.recipient:
            return {
                'id': obj.recipient.id,
                'username': obj.recipient.username,
                'email': obj.recipient.email
            }
        return None
