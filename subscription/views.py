from django.shortcuts import render
from rest_framework import viewsets 
from subscription.models import Subscription, Tag, Status, Currency
from subscription.serializers import (
  SubscriptionSerializer, TagSerializer, 
  StatusSerializer, CurrencySerializer
  )
from rest_framework.permissions import IsAuthenticated
from subscription.permissions import IsOwnerOrAdmin, IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class SubscriptionViewSet(viewsets.ModelViewSet):
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionSerializer
  permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

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

class StatusViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer
  permission_classes = [IsAuthenticated,IsAdminOrReadOnly]

class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer
  permission_classes = [IsAuthenticated, IsAdminOrReadOnly]