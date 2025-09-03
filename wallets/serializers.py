from rest_framework import serializers
from .models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Wallet
        fields = [
            'id', 'user', 'user_email', 'user_username',
            'balance', 'currency', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at', 'balance']

    def validate(self, data):
        # Bir xil valyutada faqat bitta faol hamyon bo'lishi kerak
        user = self.context['request'].user
        currency = data.get('currency')

        if Wallet.objects.filter(user=user, currency=currency, is_active=True).exists():
            raise serializers.ValidationError(
                f"You already have an active {currency} wallet."
            )

        return data