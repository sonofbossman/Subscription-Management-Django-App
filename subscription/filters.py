import django_filters
from subscription.models import Subscription
from datetime import datetime, timedelta
from django.utils import timezone

class SubscriptionFilter(django_filters.FilterSet):
  status = django_filters.CharFilter(field_name="status__name", lookup_expr="iexact")
  currency = django_filters.CharFilter(field_name="currency__code", lookup_expr="iexact")
  user = django_filters.CharFilter(field_name="user__username", lookup_expr="iexact")
  min_billing = django_filters.NumberFilter(field_name="billing_amount", lookup_expr="lte")
  max_billing = django_filters.NumberFilter(field_name="billing_amount", lookup_expr="gte")
  tags = django_filters.CharFilter(method="filter_tags")
  search_service = django_filters.CharFilter(field_name="service_name", lookup_expr="icontains")
  expiring_within_days = django_filters.NumberFilter(method="filter_expiring")

  class Meta:
    model = Subscription
    fields = [
      "user", "status", "recurring", "currency", "search_service",
      "billing_amount", "min_billing", "max_billing"
      ]
  
  def filter_tags(self, queryset, name, value):
    tags = value.split(",")
    return queryset.filter(tags__name__in=tags).distinct()
  
  def filter_expiring(self, queryset, name, value):
    today = timezone.now()
    expiring_days = today + timedelta(days=int(value))
    return queryset.filter(next_billing_date__lte=expiring_days, status__name__iexact="active")