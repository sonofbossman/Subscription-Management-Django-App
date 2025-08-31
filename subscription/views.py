from django.shortcuts import render
from rest_framework import viewsets 
from subscription.models import Subscription, Tag, Status, Currency
from subscription.serializers import (
  SubscriptionSerializer, TagSerializer, 
  StatusSerializer, CurrencySerializer
  )
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SubscriptionViewSet(viewsets.ModelViewSet):
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionSerializer
  permission_classes = [IsAuthenticated]


  def perform_create(self, serializer):
    serializer.save(user=self.request.user)

class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

class StatusViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer