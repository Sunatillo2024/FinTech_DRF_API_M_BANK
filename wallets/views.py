from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Wallet
from .serializers import WalletSerializer

class WalletListCreateView(generics.ListCreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['currency', 'is_active']  # Filter qilish uchun maydonlar
    search_fields = ['currency']  # Qidirish uchun maydonlar
    ordering_fields = ['created_at', 'balance']  # Tartiblash uchun maydonlar
    ordering = ['-created_at']  # Default tartib

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)