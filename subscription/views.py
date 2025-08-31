from django.shortcuts import render
from rest_framework import viewsets 
from subscription.models import Subscription, Tag, Status, Currency
from subscription.serializers import (
  SubscriptionSerializer, TagSerializer, 
  StatusSerializer, CurrencySerializer
  )
# Create your views here.

class SubscriptionViewSet(viewsets.ModelViewSet):
  queryset = Subscription.objects.all()
  serializer_class = SubscriptionSerializer

class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

class StatusViewSet(viewsets.ModelViewSet):
  queryset = Status.objects.all()
  serializer_class = StatusSerializer

class CurrencyViewSet(viewsets.ModelViewSet):
  queryset = Currency.objects.all()
  serializer_class = CurrencySerializer