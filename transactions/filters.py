import django_filters
from .models import Transaction
from django.utils import timezone


class TransactionFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    min_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='gte')
    max_amount = django_filters.NumberFilter(field_name='amount', lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = ['transaction_type', 'status', 'currency', 'is_fraudulent']

    def filter_recent(self, queryset, name, value):
        if value:
            return queryset.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7))
        return queryset