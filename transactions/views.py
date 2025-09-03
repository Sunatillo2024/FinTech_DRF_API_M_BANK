from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Transaction
from .serializers import TransactionSerializer

class TransactionListView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['transaction_type', 'status', 'currency', 'is_fraudulent']
    search_fields = ['description', 'transaction_type']
    ordering_fields = ['created_at', 'amount', 'updated_at']
    ordering = ['-created_at']  # Eng yangi tranzaksiyalar birinchi

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)