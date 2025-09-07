from rest_framework import viewsets, filters
from subscription.models import Subscription, Tag, Status, Currency
from subscription.serializers import (
  SubscriptionSerializer, TagSerializer, 
  StatusSerializer, CurrencySerializer
  )
from rest_framework.permissions import IsAuthenticated
from subscription.permissions import IsOwnerOrAdmin, IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from subscription.filters import SubscriptionFilter
# Create your views here.

class SubscriptionViewSet(viewsets.ModelViewSet):
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionSerializer
  permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
  filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
  # filterset_fields = ["user", "status", "recurring", "currency"]
  search_fields = ["service_name", "user"]
  ordering_fields = ["user", "billing_amount", "date_subscribed", "next_billing_date", "status"]
  ordering = ["date_subscribed"]
  filterset_class = SubscriptionFilter

  def get_queryset(self):
    user = self.request.user
    if user.is_staff:
      return Subscription.objects.all()
    return Subscription.objects.filter(user=user)

  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer
  permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
  ordering = ['id']

class StatusViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer
  permission_classes = [IsAuthenticated,IsAdminOrReadOnly]

class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer
  permission_classes = [IsAuthenticated, IsAdminOrReadOnly]