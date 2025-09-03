from django.urls import path
from .views import TransactionListView, TransactionDetailView, transfer_funds

urlpatterns = [
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('transactions/transfer/', transfer_funds, name='transfer-funds'),
]